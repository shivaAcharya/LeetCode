'''
https://www.youtube.com/watch?v=5eIK3zUdYmE
'''
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # Bellman-Ford Algorithm
        
        prices = [float("inf")] * n
        prices[src] = 0
        
        for _ in range(k + 1):
            temp_prices = prices.copy()
            
            for s, d, p in flights: # s = source, d = destionation, p = price
                # Continue if it is not possible to reach the source
                if prices[s] == float("inf"):
                    continue                
                    
                if prices[s] + p < temp_prices[d]:
                    temp_prices[d] = prices[s] + p
            
            prices = temp_prices
        
        return prices[dst] if prices[dst] != float("inf") else -1