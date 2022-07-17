class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        num_freq = Counter(nums)
        
        res = [0, 0]
        
        for v in num_freq.values():
            res[0] += (v // 2)
            res[1] += (v % 2)
        
        return res