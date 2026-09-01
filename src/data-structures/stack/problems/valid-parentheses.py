# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s: str) -> bool:
        valid_elements = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for i in s:
            if i in valid_elements:
                stack.append(i)
            else:
                if len(stack) == 0 or i != valid_elements[stack.pop()]:
                    return False
        
        if len(stack) != 0:
            return False
        
        return True
        