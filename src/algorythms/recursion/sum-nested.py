# sum-nested
arr = [1, 2, 3, [4, 5, [6, 7], 8], 9, [10]]

def solution_for_339_leetcode(n: list, depth: int = 1) -> int:
    result = 0
    for i in n:
        if isinstance(i, list):
            result += solution_for_339_leetcode(i, depth+1)
        else:
            result += i * depth

    return result

print(solution_for_339_leetcode(arr))