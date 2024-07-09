class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        
        # Populate freq
        for num, frq in counter.items():
            freq[frq].append(num)
        
        # Populate res
        res = []
        
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                res.append(num)
                
                if len(res) == k:
                    return res
        