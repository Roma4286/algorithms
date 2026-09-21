def selection_sort(arr: list[int]) -> list[int]:
    result_arr = arr.copy()

    for i in range(len(result_arr)):
        index_of_min = i
        for j in range(i + 1, len(result_arr)):
            if result_arr[j] < result_arr[index_of_min]:
                index_of_min = j

        result_arr[index_of_min], result_arr[i] = result_arr[i], result_arr[index_of_min]

    return result_arr

print(selection_sort([1, 2, 5, 3, 0, 3, 1, 20, 100, -1]))
