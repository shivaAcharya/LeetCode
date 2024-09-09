class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0] * len(temperatures)
        stack = []
        
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                _, idx = stack.pop()
                res[idx] = (i - idx)
            stack.append((temp, i))
            
        return res
    
    """
           0   1   2   3   4    5   6   7
    temp =[73, 74, 75, 71, 69, 72, 76, 73]
    stack = [(75, 2) (76, 6)]
    res = [1, 1, 4, 2, 1, 1, 0, 0]
    
    
    """
        