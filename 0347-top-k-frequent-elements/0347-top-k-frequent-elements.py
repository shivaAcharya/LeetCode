"""
1 -> 3
2 -> 2
3 -> 1

(3, 1), (2, 2), (1, 3)


"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # Bucket Sort
        counter = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        
        for num, frq in counter.items():
            freq[frq].append(num)
        
        # print(freq)
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # print(res, k)
                if len(res) == k:
                    return res                
        