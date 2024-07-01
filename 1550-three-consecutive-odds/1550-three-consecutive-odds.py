class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        
        window = []
        left = 0
        
        for right, num in enumerate(arr):
            
            if num % 2:
                window.append(True)
            else:
                window.append(False)
                
            if len(window) > 3:
                window.pop(0)
            
            if len(window) == 3 and all(window):
                return True

        return False
        