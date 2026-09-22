def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1 :
        return arr

    left = merge_sort(arr[:(len(arr) // 2)])
    right = merge_sort(arr[(len(arr) // 2):])

    i = 0
    j = 0
    result_arr = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result_arr.append(left[i])
            i += 1
        else:
            result_arr.append(right[j])
            j += 1

    result_arr += left[i:] + right[j:]
    return result_arr

print(merge_sort([1, 2, 5, 3, 0, 3, 1, 20, 100, -1]))
