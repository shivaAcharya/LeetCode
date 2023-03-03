class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        
        for i in range(len(haystack) - n + 1):
            # Two Pointer
            for j, c in enumerate(needle):
                if haystack[i+j] != c:
                    break
            else:
                return i
        
        return -1