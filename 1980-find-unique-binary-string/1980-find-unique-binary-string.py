class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        """
        Convert given array to set for constant time lookup.
        Use backtracking to create all possible binary string of length n and 
        check if the string exists in the set.
        
        """
        
        res = None
        binary_digits = []
        
        def backtrack(n):
            nonlocal res
            if res:
                return
            
            if n == len(nums):
                binary_str = "".join(binary_digits)
                if binary_str not in nums:
                    res = binary_str
                return
            
            for next_dig in '01':
                binary_digits.append(next_dig)
                backtrack(n + 1)
                binary_digits.pop()
            
        
        backtrack(0)
        
        return res
        