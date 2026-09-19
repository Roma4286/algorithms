# https://leetcode.com/problems/first-unique-character-in-a-string/
class Solution:
    def firstUniqChar(self, s: str) -> int:
        letters = {}
        for i in range(len(s)):
            if s[i] in letters:
                letters[s[i]][0] = False
            else:
                letters[s[i]] = [True, i]
        
        for letter in letters.keys():
            if letters[letter][0]:
                return letters[letter][1]
                    
        return -1