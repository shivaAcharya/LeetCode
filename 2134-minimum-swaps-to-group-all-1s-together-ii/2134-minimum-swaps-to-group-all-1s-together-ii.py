"""
nums = [0,1,1,1,0,0,1,1,0]
                l       r

max_swaps = nums.count(1) => 5

nums = [1, 1, 0, 0, 1]
                  l      r
max_swaps => 3

max_swaps = nums.count(1)
l, r = 0, 0
window = 
while l < len(nums):
    window += nums[r]
    r += 1
    # Move r till max_swaps - 1 (if r > max_swaps - 1):
    
# """
# class Solution:
#     def minSwaps(self, nums: List[int]) -> int:
#         window_size = nums.count(1)
#         min_swaps = window_size
#         l = r = 0
#         L = len(nums)
#         window_1 = 0
        
#         for r in range(window_size):
#             window_1 += nums[r]
        
        
#         for l in range(L):
#             window_1 += nums[r]
#             r += 1
#             r %= L
#             # print(r, window_1, min_swaps)
#             min_swaps = min(min_swaps, window_size - window_1)
#             window_1 -= nums[l]
#             # l += 1
        
#         return max(min_swaps, 0)

# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/solution/
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        # Initialize minimum swaps to a large value
        minimum_swaps = float("inf")

        # Calculate the total number of 1s in the array
        total_ones = sum(nums)

        # Initialize the count of 1s in the current window
        ones_count = nums[0]
        end = 0

        # Slide the window across the array
        for start in range(len(nums)):
            # Adjust ones_count by removing the element that
            # is sliding out of the window
            if start != 0:
                ones_count -= nums[start - 1]

            # Expand the window to the right until it reaches the desired size
            while end - start + 1 < total_ones:
                end += 1
                ones_count += nums[end % len(nums)]

            # Update the minimum number of swaps needed
            minimum_swaps = min(minimum_swaps, total_ones - ones_count)

        return minimum_swaps
        