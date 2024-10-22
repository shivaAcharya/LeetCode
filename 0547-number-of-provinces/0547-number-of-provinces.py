class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        N = len(isConnected)
        visited = [False] * N
        
        def dfs(city):
            visited[city] = True
            for i in range(N):
                if isConnected[city][i] and not visited[i]:
                    dfs(i)
        
        
        provinces = 0
        for i in range(N):
            if not visited[i]:
                provinces += 1
                dfs(i)
        
        return provinces
        