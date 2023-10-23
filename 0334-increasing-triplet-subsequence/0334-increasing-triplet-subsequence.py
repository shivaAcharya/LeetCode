class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        Does it have to be consecutive? => No
        
        BF: 3 for loops
        SO: Pre-process smallest on the left and largest on the right
        
        [1, 2, 3, 4, 5]
        
        [-inf, -inf, -inf, -inf, -inf]
        
        '''
        L = len(nums)
        largest_right = [float("-inf")] * L
        
        for i in range(L - 2, -1, -1):
            largest_right[i] = max(nums[i + 1], largest_right[i + 1])
        
        smallest_left = float("inf")
        for i in range(1, L):
            smallest_left = min(smallest_left, nums[i - 1])
            if smallest_left < nums[i] < largest_right[i]:
                return True
        
        return False
        
        '''
        [1, 2, 3, 4, 5]
        
        [5, 5, 5, 5, -inf]
        
        inf, 1
        '''
            
            