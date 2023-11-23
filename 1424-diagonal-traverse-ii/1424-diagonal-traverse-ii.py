class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        res = []
        matrix = rectange matrix of M = len(nums), N = max([len(arr) for arr in nums]
                filled with 0s in empty spaces
                
        Iterate on the first column
            Row -> O to M
                Col -> 0 to N
                    Add num in res if num != 0 after checking boundaries
            
        Iterate on the last row
            Row -> M - 1 to 0
                Col -> 1 to N
                    Add in res if num != 0 after checking boundaries
    
        """
        groups = defaultdict(list)
        for row in range(len(nums) - 1, -1, -1):
            for col in range(len(nums[row])):
                diagonal = row + col
                groups[diagonal].append(nums[row][col])
                
        ans = []
        curr = 0
        
        while curr in groups:
            ans.extend(groups[curr])
            curr += 1

        return ans