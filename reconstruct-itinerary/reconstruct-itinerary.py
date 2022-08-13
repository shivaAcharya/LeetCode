class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        tickets.sort(reverse=True)
        G = defaultdict(list)
        
        for u, v in tickets:
            G[u].append(v)
            
        itinerary = []
        
        def dfs(airport):
            
            while G[airport]:
                next_city = G[airport].pop()
                dfs(next_city)
            
            itinerary.append(airport)
        
        dfs('JFK')
        return reversed(itinerary)