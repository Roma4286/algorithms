# https://leetcode.com/problems/evaluate-reverse-polish-notation/
class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        operators = {
            "+": lambda x, y: x+y,
            "-": lambda x, y: x-y,
            "*": lambda x, y: x*y,
            "/": lambda x, y: int(x/y) 
            }
        stack = []
        for i in tokens:
            if i in operators:
                second_operator = stack.pop()
                first_operator = stack.pop()
                stack.append(operators[i](first_operator, second_operator))
            else:
                stack.append(int(i))
        
        return stack[0]
