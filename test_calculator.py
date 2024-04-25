import pytest
from calculator import Calculator


@pytest.fixture
def obj():
    return Calculator()


def test_order_no_member(obj):
    assert obj.calculate({"red": 1}, False) == 50
    assert obj.calculate({"green": 0}, False) == 0
    assert obj.calculate({"red": 1, "green": 1, "blue": 1}, False) == 120
    assert obj.calculate({"red": 1, "green": 1, "blue": 1, "yellow": 1, "pink": 1, "purple": 1, "orange": 1}, False) == 460


def test_order_member(obj):
    assert obj.calculate({"red": 1}, True) == 45
    assert obj.calculate({"red": 1, "green": 1, "blue": 1}, True) == 108
    assert obj.calculate({"red": 1, "green": 1, "blue": 1, "yellow": 1, "pink": 1, "purple": 1, "orange": 1}, True) == 414


def test_order_double_no_member(obj):
    assert obj.calculate({"red": 2}, False) == 100  # should not have discount
    assert obj.calculate({"orange": 2}, False) == 228
    assert obj.calculate({"orange": 2, "pink": 2}, False) == 380  # this should only get 5% discount once


def test_order_double_member(obj):
    assert obj.calculate({"red": 2}, True) == 90
    assert obj.calculate({"orange": 2}, True) == 204
    assert obj.calculate({"orange": 2, "pink": 2}, True) == 340
