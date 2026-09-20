def linear_search(arr: list[int], n: int) -> None | int:
    for i in range(len(arr)):
        if arr[i] == n:
            return i

    return None
