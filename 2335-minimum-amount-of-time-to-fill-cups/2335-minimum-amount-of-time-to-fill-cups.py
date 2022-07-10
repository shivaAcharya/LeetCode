class Solution:
    def fillCups(self, amount: List[int]) -> int:
        
        amount.sort()
        seconds = 0
        
        while sum(amount) > 0:
            amount[-1] -= 1 if amount[-1] else 0
            amount[-2] -= 1 if amount[-2] else 0
            seconds += 1
            amount.sort()
        
        return seconds