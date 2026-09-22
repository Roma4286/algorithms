import random

def quick_sort(arr: list[int], left: int = 0, right: int | None = None) -> list[int]:
    if len(arr) <= 1 :
        return arr
    
    if right is None:
        right = len(arr) - 1
        
    if right <= left:
        return arr


    curr = random.randint(left, right)
    curr_value = arr[curr]

    arr[curr], arr[right] = arr[right], arr[curr]

    n = left

    for i in range(left, right):
        if arr[i] < curr_value:
            arr[n], arr[i] = arr[i], arr[n]
            n += 1

    arr[right] = arr[n]
    arr[n] = curr_value

    quick_sort(arr, left, n - 1)
    quick_sort(arr, n + 1, right)

    return arr

print(quick_sort([1, 2, 5, 3, 0, 3, 1, 20, 100, -1]))
