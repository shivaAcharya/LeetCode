class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        
        for i in range(len(haystack) - n + 1):
            if haystack[i] == needle[0]:
                # Two Pointer
                l = i
                for c in needle:
                    if haystack[l] != c:
                        break
                    l += 1
                else:
                    return i
        
        return -1