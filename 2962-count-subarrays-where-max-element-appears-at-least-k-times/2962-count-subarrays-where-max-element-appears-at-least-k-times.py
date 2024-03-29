# nums = [1,3,2,3,3], k = 2


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_element = max(nums)
        left = res = max_element_count = 0
        
        for right, num in enumerate(nums):
            if num == max_element:
                max_element_count += 1
            
            while max_element_count == k:
                if nums[left] == max_element:
                    max_element_count -= 1
                left += 1
            
            res += left
        
        return res            
            