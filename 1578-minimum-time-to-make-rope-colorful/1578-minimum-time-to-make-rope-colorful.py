class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        i = cost = 0
        L = len(colors)
        
        while i < L:
            running_sum = max_time = neededTime[i]
            i += 1
            while i < L and colors[i] == colors[i - 1]:
                running_sum += neededTime[i]
                max_time = max(max_time, neededTime[i])
                i += 1
            else:
                cost += (running_sum - max_time)
                
        return cost
    