class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        ticket_graph = defaultdict(list)
        sorted_tickets = sorted(tickets, reverse=True)
        for start, end in sorted_tickets:
            ticket_graph[start].append(end)
            
        route = []
        def visit(airport, ticket_graph, route):
            while ticket_graph[airport]:
                next_city = ticket_graph[airport].pop()
                visit(next_city, ticket_graph, route)
            route.append(airport)
        
        
        visit('JFK', ticket_graph, route)
        route.reverse()
        return route



        