def merge_sort(arr, left=0, right=None):
    if right is None:
        right = len(arr)
    if right > left + 1:
        middle = (left + right) // 2
        merge_sort(arr, left, middle)
        merge_sort(arr, middle, right)
        merge(arr, left, middle, right)
        return arr


def merge(arr, left, middle, right):
    n1 = middle - left
    n2 = right - middle
    left_arr = arr[left:middle]
    right_arr = arr[middle:right]
    i = j = 0
    k = left
    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1


arr = [3, 7, 2, 8, 1, 9, 4, 6, 11, 10, 5]

print(merge_sort(arr))
