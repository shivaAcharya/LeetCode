class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        
        res = []
                
        for k, trim in queries:
            # Create trimmed_nums array after trimming
            trimmed_nums = [num[-trim:] for num in nums]
            
            # Create num_idx with pair of num and it's index
            num_idx = [(num, i) for i, num in enumerate(trimmed_nums)]
            
            # Find kth smallest using heapq and apped the index to res
            res.append(heapq.nsmallest(k, num_idx)[-1][-1])
        
        return res    
        