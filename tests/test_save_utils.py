import os
import tempfile
import pytest
from src.save_utils import save_results


class TestSaveResults:
    def test_save_results_basic(self):
        alive = ["example.com", "sub.example.com"]
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            filename = f.name
        try:
            save_results(alive, filename)
            with open(filename, "r") as f:
                content = f.read()
            expected = "example.com\nsub.example.com\n"
            assert content == expected
        finally:
            os.unlink(filename)

    def test_save_results_empty(self):
        alive = []
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            filename = f.name
        try:
            save_results(alive, filename)
            with open(filename, "r") as f:
                content = f.read()
            assert content == ""
        finally:
            os.unlink(filename)

    def test_save_results_sorted(self):
        alive = ["z.example.com", "a.example.com"]
        with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
            filename = f.name
        try:
            save_results(alive, filename)
            with open(filename, "r") as f:
                content = f.read()
            expected = "a.example.com\nz.example.com\n"
            assert content == expected
        finally:
            os.unlink(filename)
