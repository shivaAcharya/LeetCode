class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_indices = defaultdict(list)
        
        for i, num in enumerate(nums):
            cur_sum = 0
            while num:
                cur_sum += (num % 10)
                num //= 10
            if len(sum_indices[cur_sum]) < 2:            
                sum_indices[cur_sum].append(nums[i])
            elif nums[i] >= min(sum_indices[cur_sum]):
                sum_indices[cur_sum].append(nums[i])
                sum_indices[cur_sum].remove(min(sum_indices[cur_sum]))
            
        res = -1 
        print(sum_indices)
        for lst in sum_indices.values():
            if len(lst) > 1:
                res = max(res, lst[-1] + lst[-2])
        
        return res