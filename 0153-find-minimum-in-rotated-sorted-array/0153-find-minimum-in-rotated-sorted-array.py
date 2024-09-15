"""
                    l        
                 m        
                    r
nums = [4, 5, 6, 7, 0, 1, 2]
                    ^


"""
class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        
            # print(l)
        return nums[l]
    
"""
          l
          m
             r
[3, 4, 5, 1, 2]

 0  1  2  3  4

"""