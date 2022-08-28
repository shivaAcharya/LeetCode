class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        '''
        1. Use topological sort to create rows, and cols array.
        2. Build matrix based on rows, and cols array.
        '''
        
        def topo_sort(lst):
            arr = []
            G = defaultdict(set)
            indegrees = Counter()
            lst = set([tuple(a) for a in lst])
            for u, v in lst:
                G[u].add(v)
                indegrees[v] += 1
                
            seen = set()
            
            Q = deque()
            # Populate Q
            for i in range(1, k + 1):
                if indegrees[i] == 0:
                    Q.append(i)
                    seen.add(i)
            
            #print(G, indegrees, seen, Q)
                    
            while Q:
                num = Q.popleft()
                arr.append(num)
                
                for nei in G[num]:        
                    indegrees[nei] -= 1
                    if indegrees[nei] == 0 and nei not in seen:
                        Q.append(nei)
                        seen.add(nei)
            
            return arr if len(seen) == k else []
        
        
        rows = topo_sort(rowConditions)
        cols = topo_sort(colConditions)
        
       
        if not rows or not cols:
            return
        
        
        res = [[0] * k for _ in range(k)]
        
        for i in range(1, k + 1):
            res[rows.index(i)][cols.index(i)] = i
        
        return res
                
                
                
                
                
                
                
                
                
                
                
                
                
                
            