def binary_search(arr: list[int], n: int) -> None | int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == n:
            return mid

        if arr[mid] < n:
            left = mid + 1
        else:
            right = mid - 1

    return None

