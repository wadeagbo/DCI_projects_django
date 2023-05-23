from   quicksort  import quicksort

def test_Pquickshort():
    arr = [3, 7, 2, 8, 1, 9, 4, 6]
    quicksort(arr)
    assert arr == [1, 2, 3, 4, 6, 7, 8, 9]
