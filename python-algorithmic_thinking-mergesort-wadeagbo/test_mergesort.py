from mergesort import merge_sort


def test_mergesort():
    arr = [3, 7, 2, 8, 1, 9, 4, 6]
    merge_sort(arr)
    assert arr == [1, 2, 3, 4, 6, 7, 8, 9]
