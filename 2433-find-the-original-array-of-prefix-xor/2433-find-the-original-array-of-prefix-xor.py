class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        """
        
        
        
        """
        res = []
        running_xor = 0
        
        for num in pref:
            cur_xor = running_xor ^ num
            res.append(cur_xor)
            running_xor ^= cur_xor
        
        return res