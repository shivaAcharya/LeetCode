"""
counter = {num -> freq}

1 -> 3
2 -> 2
3 -> 1
-------
4 -> 2

k = 2

       0    1   2   3   4   5   6
freq = [[], [3], [2], [1], [], [], []]
res = [1]


"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, frq in counter.items():
            freq[frq].append(num)
        
        res = []
        print(freq) # [[], [1]]
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                print(res)
                if len(res) == k:
                    return res
                