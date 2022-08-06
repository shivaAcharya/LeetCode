class Solution:
    def partition(self, s: str) -> List[List[str]]:
        results = []
        candidate = []
    
        def search(i):
            if i == len(s):
                results.append(candidate[:])
                return
            for j in range(i+1, len(s) + 1):
                sub = s[i:j]
                if isPalindrome(sub):
                    candidate.append(sub)
                    search(j)
                    candidate.pop()
        def isPalindrome(s):
            for i in range(len(s)//2):
                if s[i] != s[len(s)-1-i]:
                    return False
            return True
        
        search(0)
        return results
        