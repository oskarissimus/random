from sort_algo.quick_sort import quick_sort
import pytest
from hypothesis import given, strategies as st


@pytest.mark.parametrize(
    "l,expected",
    [
        ([1], [1]),
        ([1, 2], [1, 2]),
        ([2, 1], [1, 2]),
    ],
)
def test_quick_sort(l, expected):
    assert quick_sort(l) == expected


@given(st.lists(st.integers()))
def test_quick_sort_returns_the_same(l):
    assert sorted(l) == quick_sort(l)
