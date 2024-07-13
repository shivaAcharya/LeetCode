"""

counter = {
    1 => 3,
    2 => 2,
    3 => 1
}

freq = [[], [3], [2], [1], [], [], []]
        0   1    2    3    4   5   6

res = [1, 2]

        
"""

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n, f in counter.items():
            freq[f].append(n)
            
        res = []
        
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                
                if len(res) == k:
                    return res
        