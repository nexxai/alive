import pytest
from src.cert_utils import fetch_certs, extract_hostnames


class TestFetchCerts:
    def test_fetch_certs_success(self, mocker):
        mock_response = mocker.Mock()
        mock_response.json.return_value = [{"name_value": "example.com"}]
        mock_response.raise_for_status.return_value = None
        mocker.patch("requests.get", return_value=mock_response)

        result = fetch_certs("example.com")
        assert result == [{"name_value": "example.com"}]

    def test_fetch_certs_error(self, mocker):
        mocker.patch("requests.get", side_effect=Exception("API error"))
        with pytest.raises(Exception):
            fetch_certs("example.com")


class TestExtractHostnames:
    def test_extract_hostnames_basic(self):
        certs = [
            {"name_value": "example.com"},
            {"name_value": "sub.example.com"},
            {"name_value": "*.example.com"},  # should be excluded
        ]
        result = extract_hostnames(certs)
        expected = {"example.com", "sub.example.com"}
        assert result == expected

    def test_extract_hostnames_empty(self):
        certs = []
        result = extract_hostnames(certs)
        assert result == set()

    def test_extract_hostnames_duplicates(self):
        certs = [
            {"name_value": "example.com"},
            {"name_value": "example.com"},
        ]
        result = extract_hostnames(certs)
        assert result == {"example.com"}

    def test_extract_hostnames_case_insensitive(self):
        certs = [
            {"name_value": "Example.Com"},
            {"name_value": "example.com"},
        ]
        result = extract_hostnames(certs)
        assert result == {"example.com"}
