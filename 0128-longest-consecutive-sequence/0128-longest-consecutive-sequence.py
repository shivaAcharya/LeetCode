class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        cur_seq = max_seq = 0
        
        for num in nums_set:
            cur_seq = 1
            # Check if num is the start of a sequence
            if num - 1 not in nums_set:
                # Calculate the length of the sequence
                while num + 1 in nums_set:
                    num += 1
                    cur_seq += 1
            
            max_seq = max(max_seq, cur_seq)
        
        return max_seq        
        