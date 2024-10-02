class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num_arr = defaultdict(list)
        
        for i, num in enumerate(arr):
            num_arr[num].append(i)
            
        sorted_arr = sorted(arr)
        rank = [1] * len(arr)
        
        for i, num in enumerate(sorted_arr):
            if i > 0:
                if num == sorted_arr[i - 1]:
                    rank[i] = rank[i - 1]
                else:
                    rank[i] = 1 + rank[i - 1]
        
        res = [0] * len(arr)
        
        for r, n in zip(rank, sorted_arr):
            res[num_arr[n].pop()] = r
        
        return res        
        