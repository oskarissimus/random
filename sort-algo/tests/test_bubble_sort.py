from sort_algo.bubble_sort import bubble_sort
import pytest

@pytest.mark.parametrize("nums,expected",(
        ([1,3,2],[1,2,3]),
        ([1,3,2],[1,2,3]),
        ([1],[1])
))
def test_bubble_sort(nums,expected):
    assert bubble_sort(nums) == expected

from hypothesis import given, strategies as st

@given(st.lists(st.integers()))
def test_bubble_sort(nums):
    assert sorted(nums) == bubble_sort(nums)