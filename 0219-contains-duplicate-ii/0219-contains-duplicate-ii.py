class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        num_idx = {}
        
        for idx, num in enumerate(nums):
            if num in num_idx and abs(num_idx[num] - idx) <= k:
                return True
            num_idx[num] = idx
        
        return False