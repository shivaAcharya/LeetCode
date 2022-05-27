class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        # Handle edge case
        if not digits:
            return res        
        
        mnemonic = []
        mapping = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        def backtrack(idx):
            if len(mnemonic) == len(digits):
                res.append("".join(mnemonic))
                return
            
            for letter in mapping[digits[idx]]:
                mnemonic.append(letter)
                backtrack(idx+1)
                mnemonic.pop()
        
        backtrack(0)
        return res
                