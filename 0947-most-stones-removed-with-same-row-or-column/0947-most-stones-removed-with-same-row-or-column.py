class Solution:
    '''
    https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/solution/
    '''
    ################## DFS ######################
    
    def removeStones(self, stones: List[List[int]]) -> int:
        
        # Build Graph
        G = defaultdict(list)
        
        L = len(stones)
        for i in range(L-1):
            for j in range(i + 1, L):
                # Check if share same row or column
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    G[i].append(j)
                    G[j].append(i)
        
        def dfs(stone):
            
            visited.add(stone)
            
            for nei in G[stone]:
                if nei not in visited:
                    dfs(nei)
            
        
        components = 0
        visited = set()
        
        for i in range(L):
            if i not in visited:
                dfs(i)
                components += 1
        
        return L - components