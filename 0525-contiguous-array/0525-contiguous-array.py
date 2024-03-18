class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        """
        Examples:
        1.  Input: nums = [0, 0, 1, 0, 0, 1, 1, 1, 0]
            Output: 4
        
        2.  Input: nums = [1, 1, 0, 1, 0, 0, 0]
        
        """
        
        count_index = {0:-1}
        
        max_length = count = 0
        
        for i, num in enumerate(nums):
            if num:
                count += 1
            else:
                count -= 1
            
            if count in count_index:
                cur_length = i - count_index[count]
                if cur_length > max_length:
                    max_length = cur_length
            else:
                count_index[count] = i
        
        return max_length