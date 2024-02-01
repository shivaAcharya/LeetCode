class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):

            while stack and stack[-1][-1] < temp:
                prev_i, prev_tmp = stack.pop()
                ans[prev_i] = i - prev_i
            
            stack.append((i, temp))
        
        return ans