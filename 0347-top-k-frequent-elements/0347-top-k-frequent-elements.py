"""
Can k > len(nums)? => No

counter = {}
max_heap
nlargest(n, N) => O(N*logn)

1 -> 3
2 -> 2
6 -> 2
3 -> 1

k = 2

0, 1, 2, 3, 4   N
[] [3] [2, 6] [1] [] []

res = [2, 6]

"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counter = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, frq in counter.items():
            freq[frq].append(num)
        
        res = []
        for arr in reversed(freq):
            for n in arr:
                res.append(n)
                if len(res) == k:
                    return res
