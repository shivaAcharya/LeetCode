class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        count = 0

        for i in range(len(nums) - 2):
            
            l, r = i + 1, len(nums) - 1
            
            while l < r:
                cur_sum = nums[i] + nums[l] + nums[r]
                
                if cur_sum < target:
                    # IMPORTANT
                    # TRICKY PART HERE
                    # IF THREESUM < TARGET, THEN BECAUSE THEE ARRAY IS SORTED
                    # ALL NUMBERS IN BETWEEN WILL ALSO BE LESS OR EQUAL TO K
                    # AND THEREFORE BE VALID ANSWERS
                    
                    count += r - l
                    l += 1
                else:
                    r -= 1
        
        return count