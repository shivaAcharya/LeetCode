from functools import cmp_to_key
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        def compare(a, b):
            if abs(a - x) > abs(b - x):
                return 1

            if abs(a - x) == abs(b - x) and a > b:
                return 1
                
            return -1
        
        arr.sort(key=cmp_to_key(compare))
        
        return sorted(arr[:k])
        '''
        
        return sorted(sorted(arr, key = lambda num : abs(x - num))[:k])