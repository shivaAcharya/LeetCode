class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        
        # Calculate running minimum from the end
        min_array = [0] * len(arr)
        min_array[-1] = arr[-1]
        
        for i in range(len(arr) - 2, -1, -1):
            min_array[i] = min(min_array[i+1], arr[i])
        
        # Calculate running max from the front and update chunks
        chunks = 1
        
        max_so_far = 0
        for i in range(len(arr) - 1):
            max_so_far = max(max_so_far, arr[i])
            
            if max_so_far < min_array[i+1]:
                chunks += 1
        
        return chunks