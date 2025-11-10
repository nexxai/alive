import sys
import pytest
from unittest.mock import patch
from main import main


class TestMain:
    @patch("main.save_results")
    @patch("main.check_alive")
    @patch("main.extract_hostnames")
    @patch("main.fetch_certs")
    def test_main_success(
        self, mock_fetch, mock_extract, mock_check, mock_save, capsys
    ):
        mock_fetch.return_value = [{"name_value": "example.com"}]
        mock_extract.return_value = {"example.com"}
        mock_check.return_value = ["example.com"]

        # Mock sys.argv
        with patch.object(sys, "argv", ["main.py", "example.com"]):
            main()

        # Check prints
        captured = capsys.readouterr()
        assert "Fetching certificates for example.com" in captured.out
        assert "Fetched 1 certificates" in captured.out
        assert "Extracted 1 unique hostnames" in captured.out
        assert "Found 1 alive domains" in captured.out
        assert "Saving results" in captured.out

        mock_fetch.assert_called_once_with("example.com")
        mock_extract.assert_called_once_with([{"name_value": "example.com"}])
        mock_check.assert_called_once_with({"example.com"})
        mock_save.assert_called_once()

    @patch("main.fetch_certs")
    def test_main_fetch_error(self, mock_fetch, capsys):
        mock_fetch.side_effect = Exception("API error")

        with patch.object(sys, "argv", ["main.py", "example.com"]):
            with pytest.raises(SystemExit):
                main()

        captured = capsys.readouterr()
        assert "Error fetching from crt.sh: API error" in captured.out
