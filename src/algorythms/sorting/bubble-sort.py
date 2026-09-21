def bubble_sort(arr: list[int]) -> list[int]:
    result_arr = arr.copy()
    for i in range(len(result_arr)):
        swapped = False

        for j in range(1, len(result_arr) - i):
            if result_arr[j] < result_arr[j - 1]:
                result_arr[j], result_arr[j-1] = result_arr[j-1], result_arr[j]
                swapped = True

        if not swapped:
            break

    return result_arr

print(bubble_sort([1, 2, 5, 3, 0, 3, 1, 20, 100, -1]))
