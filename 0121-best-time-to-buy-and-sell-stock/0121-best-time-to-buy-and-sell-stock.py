"""
prices = [7,1,5,3,6,4]

cur_low = 1
max_profit = 5


"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cur_low = float("inf")
        max_profit = 0
        
        for price in prices:
            if price < cur_low:
                cur_low = price
            else:
                max_profit = max(max_profit, price - cur_low)
        
        return max_profit
        