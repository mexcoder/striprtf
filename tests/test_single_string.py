import pytest
from pathlib import Path

from striprtf.striprtf import rtf_to_text

RTF_DIR = Path.cwd() / "tests" / "rtf"
TEXT_DIR = Path.cwd() / "tests" / "text"


class TestSingleStrings:

    strings = [
         (r"\'f3", "ó"),
         (r"\'f1", "ñ"),
        (r"caf\'e9", "café"),
        (r"Champi\'f1ones", "Champiñones"),
        (r"camar\'f3n, at\'fan o jam\'f3n", "camarón, atún o jamón"),
        (r"Bet\'fan de Caf\'e9.", "Betún de Café.")
    ]

    @pytest.mark.parametrize("test,expected", strings)
    def test_strings(self, test, expected):
        result = rtf_to_text(test)
        assert expected == result

