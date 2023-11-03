class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        mapping = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz',
        }
        
        res = []
        if not digits:
            return res
        letters = []
        def backtrack(i):
            # End case
            if i == len(digits):
                res.append("".join(letters))
                return
            
            for c in mapping[digits[i]]:
                letters.append(c)
                backtrack(i+1)
                letters.pop()
        
        backtrack(0)
        return res
        