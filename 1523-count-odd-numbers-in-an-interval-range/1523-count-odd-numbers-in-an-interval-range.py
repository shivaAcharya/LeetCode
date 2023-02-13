class Solution:
    def countOdds(self, low: int, high: int) -> int:
        res = math.ceil((high - low) / 2)
        
        return res + 1 if low % 2 and high % 2 else res