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


def solution_for_364_leetcode(n: list) -> int:
    sum_arr = []

    def func(n: list, depth: int = 0) -> int:
        for i in n:
            if isinstance(i, list):
                func(i, depth+1)
            else:
                while depth > len(sum_arr) - 1:
                    sum_arr.append(0)
                sum_arr[depth] += i

    func(n)

    result = 0
    for i in range(len(sum_arr)):
        result += (len(sum_arr) - i) * sum_arr[i]

    return result
    

print(solution_for_339_leetcode(arr))
print(solution_for_364_leetcode(arr))