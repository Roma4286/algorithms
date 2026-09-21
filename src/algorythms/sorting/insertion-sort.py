def insertion_sort(arr: list[int]) -> list[int]:
    result_arr = arr.copy()

    for i in range(len(result_arr)):
        j = i
        curr = result_arr[j]
        while j > 0 and curr < result_arr[j - 1]:
            result_arr[j] = result_arr[j - 1]
            j -= 1

        result_arr[j] = curr

    return result_arr

print(insertion_sort([1, 2, 5, 3, 0, 3, 1, 20, 100, -1]))
