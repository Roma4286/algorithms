# https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = []
        indexes_of_str = {}

        for i in strs:
            counts = [0] * 26

            a = ord('a')
            for letter in i:
                counts[ord(letter) - a] += 1

            index = tuple(counts)
            if index in indexes_of_str:
                result[indexes_of_str[index]].append(i)
            else:
                result.append([i])
                indexes_of_str[index] = len(result)-1
        
        return result