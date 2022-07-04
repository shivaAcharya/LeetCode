class Solution:
    def candy(self, ratings: List[int]) -> int:
        res = 1
        up = down = peak = 0
        
        for i in range(1, len(ratings)):
            if ratings[i-1] < ratings[i]:
                up += 1
                peak = up
                down = 0
                res += up + 1
            
            elif ratings[i-1] == ratings[i]:
                peak = up = down = 0
                res += 1
            
            else:
                up = 0
                down += 1
                res += 1 + down + (-1 if peak >= down else 0)

        return res