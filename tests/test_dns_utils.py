import socket
import pytest
from src.dns_utils import check_alive


class TestCheckAlive:
    def test_check_alive_resolving(self, mocker):
        hostnames = ["example.com", "nonexistent.example"]
        mocker.patch("socket.gethostbyname", side_effect=["1.2.3.4", socket.gaierror])
        result = check_alive(hostnames)
        assert result == ["example.com"]

    def test_check_alive_none_resolving(self, mocker):
        hostnames = ["nonexistent1.example", "nonexistent2.example"]
        mocker.patch("socket.gethostbyname", side_effect=socket.gaierror)
        result = check_alive(hostnames)
        assert result == []

    def test_check_alive_all_resolving(self, mocker):
        hostnames = ["example.com", "google.com"]
        mocker.patch("socket.gethostbyname", return_value="1.2.3.4")
        result = check_alive(hostnames)
        assert result == hostnames

    def test_check_alive_empty_list(self, mocker):
        hostnames = []
        result = check_alive(hostnames)
        assert result == []
