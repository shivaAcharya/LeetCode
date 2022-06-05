class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        
        num_idx = {num : idx for idx, num in enumerate(nums)}
        
        for first, second in operations:
            idx = num_idx[first]
            nums[idx] = second
            num_idx[second] = idx
        
        return nums