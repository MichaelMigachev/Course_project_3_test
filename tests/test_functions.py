import pytest
from utils import functions

def test_list_operations():
    with pytest.raises(FileNotFoundError):
        assert functions.list_operations() == None


def test_date_time():
    assert functions.date_time("2019-08-26T10:50:58.294041") == "08.26.2019"

def test_card_number():
    assert functions.card_number("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"

def test_check_number():
    assert functions.check_number("Счет 64686473678894779589") == "Счет **9589"

