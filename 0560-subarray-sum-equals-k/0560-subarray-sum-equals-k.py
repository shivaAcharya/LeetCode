class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = cur_sum = 0
        h = defaultdict(int)
        
        for n in nums:
            cur_sum += n
            
            if cur_sum == k:
                count += 1
            
            count += h[cur_sum - k]
            h[cur_sum] += 1
        
        return count