class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
        if len(num) == 1:
            return num in "018"
        
        l, r = 0, len(num) - 1
        
        while l <= r:
            
            if num[l] not in "01689" or num[r] not in "01689":
                return False

            if num[l] != num[r] and (num[l] not in "69" or num[r] not in "69"):
                return False
                
            if num[l] == '6' and num[r] != '9':
                return False
            
            if num[l] == '9' and num[r] != '6':
                return False
            
            if l == r and num[l] not in "018":
                return False            
            
            l += 1
            r -= 1
        
        return True