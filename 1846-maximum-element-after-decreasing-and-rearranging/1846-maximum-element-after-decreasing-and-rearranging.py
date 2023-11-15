class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        """
        Sort the given array.
        Return the max(array[-1], len(array))
        
        """
        
        arr.sort()
        ans = 1
        
        for num in arr[1:]:
            if num >= ans + 1:
                ans += 1
        
        return ans
        