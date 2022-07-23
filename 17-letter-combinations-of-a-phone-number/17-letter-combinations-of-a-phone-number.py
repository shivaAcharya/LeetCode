class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapping = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl", "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
        
        res = []
        mnemonics = []
        
        # Edge case
        if not digits:
            return res
        
        def helper(i):
            
            if len(mnemonics) == len(digits):
                res.append("".join(mnemonics))
                return
            
            digit = digits[i]
            
            for c in mapping[digit]:
                mnemonics.append(c)
                
                helper(i+1)
                
                mnemonics.pop()
            

        helper(0)
        
        return res