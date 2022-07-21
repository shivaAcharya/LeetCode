class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        min_array = [0] * len(arr)
        min_array[-1] = arr[-1]
        chunks = 1
        
        # Calculate running min from the end
        for i in range(len(arr) - 2, -1, -1):
            min_array[i] = min(arr[i], min_array[i+1])
        
        # Calculate max_so_far from the front and chunks
        max_so_far = arr[0]
        for i in range(len(arr) - 1):
            max_so_far = max(max_so_far, arr[i])
            if max_so_far <= min_array[i + 1]:
                chunks += 1

        
        return chunks