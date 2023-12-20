class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        prices.sort()
        left_over = money - (prices[0] + prices[1])
        
        return left_over if left_over >= 0 else money
    