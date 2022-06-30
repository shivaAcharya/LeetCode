class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        new_shifts = shifts[::]
        #print(new_shifts)
        for i in range(len(new_shifts) - 2, -1, -1):
            new_shifts[i] += new_shifts[i+1]
    
        #print(new_shifts)
        
        res = []
        
        for i, letter in enumerate(s):
            idx = alphabets.index(letter)
            idx_shift = (idx + new_shifts[i]) % 26
            res.append(alphabets[idx_shift])
        
        return "".join(res)
        
        