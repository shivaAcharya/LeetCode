class Solution:
    def minSteps(self, s: str, t: str) -> int:
        letters = [0] * 26
        
        for c1, c2 in zip(s, t):
            letters[ord(c1) - ord('a')] += 1
            letters[ord(c2) - ord('a')] -= 1
        
        print(letters)
        ans = 0
        for letter in letters:
            if letter > 0:
                ans += letter
        
        return ans
        