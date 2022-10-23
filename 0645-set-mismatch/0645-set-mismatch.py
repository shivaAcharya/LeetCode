class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        s = set()
        res = []
        
        # Find Duplicate
        for num in nums:
            if num in s:
                res.append(num)
            s.add(num)
            
        # Find Missing
        for i in range(1, len(nums) + 1):
            if i not in s:
                res.append(i)
                break
                
                
        return res