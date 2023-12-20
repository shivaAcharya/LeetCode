class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        first_min = second_min = 101
        
        for price in prices:
            if price < first_min:
                first_min, second_min = price, first_min
            elif price < second_min:
                second_min = price            
        
        left_over = money - (first_min + second_min)
        
        return left_over if left_over >= 0 else money
    