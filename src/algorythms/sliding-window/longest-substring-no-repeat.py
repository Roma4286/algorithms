from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = deque()
        elements = {}
        max_len = 0
        for i in range(len(s)):
            if s[i] in elements:
                max_len = max(len(queue), max_len)
                
                element = queue.popleft()
                del elements[element]
                while element != s[i]:
                    element = queue.popleft()
                    del elements[element]
            
            elements[s[i]] = i
            queue.append(s[i])
        
        max_len = max(len(queue), max_len)
        
        return max_len