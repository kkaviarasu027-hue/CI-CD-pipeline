import pytest
from app import add_numbers, get_status

def test_add_logic():
    assert add_numbers(10, 5) == 15
    assert add_numbers(-1, 1) == 0

def test_status_logic():
    assert get_status() == "Active"