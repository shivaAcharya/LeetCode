class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        
        memo = [0] * (amount + 1)
        
        def makeChange(change):
            if change < 0: return -1
            if change == 0: return 0
            
            if memo[change] > 0:
                return memo[change]
            
            min_change = float("inf")
            
            for coin in [c for c in coins if c <= change]:
                num_coins = 1 + makeChange(change - coin)
                min_change = min(min_change, num_coins)
                memo[change] = min_change
            return min_change
        
        res = makeChange(amount)
        return res if res != float("inf") else -1
            
                