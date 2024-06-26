import pytest
from sort_algo.merge_sort import merge, merge_sort
from hypothesis import given, strategies as st


@pytest.mark.parametrize(
    "l,expected",
    [
        ([1, 2], [1, 2]),
        ([2, 1], [1, 2]),
        ([2, 1, 3], [1, 2, 3]),
    ],
)
def test_merge_sort(l, expected):
    assert merge_sort(l) == expected


@pytest.mark.parametrize(
    "l1,l2,expected",
    [
        ([1], [2], [1, 2]),
        ([1, 3], [2], [1, 2, 3]),
        ([1, 2], [3], [1, 2, 3]),
        ([2, 3], [1], [1, 2, 3]),
    ],
)
def test_merge(l1, l2, expected):
    assert merge(l1, l2) == expected
    assert merge(l2, l1) == expected


@given(st.lists(st.integers()))
def test_sort_returns_the_same_as_builtin(l):
    assert sorted(l) == merge_sort(l)
