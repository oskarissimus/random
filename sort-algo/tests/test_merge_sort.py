from sort_algo.merge_sort import merge, merge_sort


def test_merge_sort():
    assert merge_sort([2, 1]) == [1, 2]


def test_merge():
    assert merge([1], [2]) == [1, 2]
