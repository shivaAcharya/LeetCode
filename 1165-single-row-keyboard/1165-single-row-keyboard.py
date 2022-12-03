class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        char_idx = {k : v for v, k in enumerate(keyboard)}
        
        cur_idx = time_taken = 0
        
        for char in word:
            time_taken += abs(cur_idx - char_idx[char])
            cur_idx = char_idx[char]
        
        return time_taken