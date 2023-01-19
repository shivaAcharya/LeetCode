'''
Topological Sort

1. Intialize an empty defaultdict G, and indegrees with all letters mapped to 0.
2. Build G and maintain indegrees using two consecutive words from words list.
3. Initialize Q with letters with 0 indegree
4. Perform BFS building res list.
5. Return res if len(res) == len(indegrees), otherwise ""

'''

class Solution:
    def alienOrder(self, words: List[str]) -> str:

        indegrees = Counter({c : 0 for word in words for c in word})
        G = defaultdict(set)

        # Build G and maintain indegrees
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i + 1]
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in G[c1]:
                        G[c1].add(c2)
                        indegrees[c2] += 1
                    break
            else:
                if len(word2) < len(word1):
                    return ""
        
        # Initialize Q
        Q = deque([c for c, indegree in indegrees.items() if indegree == 0])

        res = []
        #print(indegrees, G)
        while Q:
            c = Q.popleft()
            res.append(c)

            for nc in G[c]:
                indegrees[nc] -= 1
                if indegrees[nc] == 0:
                    Q.append(nc)
        
        return "".join(res) if len(res) == len(indegrees) else ""
    
"""
Time => O(V + E)
Space => O(V + E)
"""
            
