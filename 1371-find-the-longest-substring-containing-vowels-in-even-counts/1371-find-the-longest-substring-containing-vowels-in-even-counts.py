"""

l
        r
e l e e t m i n i c o w o r o e p


"""
# https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/solution/
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        prefixXOR = 0
        characterMap = [0] * 26
        characterMap[ord("a") - ord("a")] = 1
        characterMap[ord("e") - ord("a")] = 2
        characterMap[ord("i") - ord("a")] = 4
        characterMap[ord("o") - ord("a")] = 8
        characterMap[ord("u") - ord("a")] = 16
        mp = [-1] * 32
        longestSubstring = 0
        for i in range(len(s)):
            prefixXOR ^= characterMap[ord(s[i]) - ord("a")]
            if mp[prefixXOR] == -1 and prefixXOR != 0:
                mp[prefixXOR] = i
            longestSubstring = max(longestSubstring, i - mp[prefixXOR])
        return longestSubstring
        