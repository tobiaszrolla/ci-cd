from src.utils import add, sub, mult, div
import pytest


@pytest.mark.parametrize(
    "a, b, expected ", [(1, 2, 3), (2, 3, 5), (3, 4, 7), (4, -5, -1)]
)
def test_add(a, b, expected):
    result = add(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(5, 2, 3), (1, 3, -2), (145, 20, 125), (2, 15, -13)]
)
def test_sub(a, b, expected):
    result = sub(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(7, 8, 56), (2, 3, 6), (3, 7, 21), (-2, 5, -10)]
)
def test_mult(a, b, expected):
    result = mult(a, b)
    assert result == expected


@pytest.mark.parametrize(
    "a, b, expected ", [(2, 1, 2), (5, 2, 2.5), (1, -4, -0.25), (1, 1, 1)]
)
def test_div(a, b, expected):
    result = div(a, b)
    assert result == expected
