# https://leetcode.com/problems/permutation-in-string
from collections import deque

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        original_counts_of_el = {}
        for i in s1:
            if i in original_counts_of_el:
                original_counts_of_el[i] += 1
            else: 
                original_counts_of_el[i] = 1
        
        counts_of_el = original_counts_of_el.copy()
        queue = deque()
        for i in range(len(s2)):
            if s2[i] in counts_of_el:
                count = counts_of_el[s2[i]] - 1
                if count >= 0:
                    if len(queue)+1 == len(s1):
                        return True
                else:
                    el = queue.popleft()
                    counts_of_el[el] += 1
                    while el != s2[i]:
                        el = queue.popleft()
                        counts_of_el[el] += 1

                queue.append(s2[i])
                counts_of_el[s2[i]] = counts_of_el[s2[i]] - 1

            else:
                if len(s2)-i < len(s1):
                    return False
                counts_of_el = original_counts_of_el.copy()
                queue = deque()

        return False