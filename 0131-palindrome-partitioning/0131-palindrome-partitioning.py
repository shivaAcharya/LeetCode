class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        results = []
        candidates = []
        
        def backtrack(i):
            if i == len(s):
                results.append(candidates[:])
                return
            
            for j in range(i + 1, len(s) + 1):
                sub = s[i : j]
                if is_palindrome(sub):
                    candidates.append(sub)
                    backtrack(j)
                    candidates.pop()
        
        
        def is_palindrome(s):
            for i in range(len(s) // 2):
                if s[i] != s[len(s) - 1 - i]:
                    return False
            return True
        
        backtrack(0)
        return results