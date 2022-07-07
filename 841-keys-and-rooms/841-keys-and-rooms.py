class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited_rooms = set()
        G = defaultdict(list)
        # Build Graph
        # rooms = [[1,3],[3,0,1],[2],[0]]
        """
        # G = {
            0 : [1, 3]
            1 : [3, 0, 1]
            2 : [2]
            3 : [0]
            4 : []
        }
        """
        for room, keys in enumerate(rooms):
            G[room] = keys
        

        def dfs(source):
            if source in visited_rooms:
                return 
            
            visited_rooms.add(source)
            
            for neighbor in G[source]:
                dfs(neighbor)
                

        dfs(0)
        print(len(visited_rooms))
        
        return len(visited_rooms) == len(rooms)