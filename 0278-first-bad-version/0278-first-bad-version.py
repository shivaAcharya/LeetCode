# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        l = 1
        
        while l < n:
            mid = (l + n) // 2
            
            if not isBadVersion(mid):
                l = mid + 1
            else:
                n = mid
        
        return l