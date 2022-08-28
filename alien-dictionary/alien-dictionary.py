class Solution:
    def alienOrder(self, words: List[str]) -> str:
        
        indegrees = {c : 0 for word in words for c in word}
        G = defaultdict(set)
        
        # Build Graph
        
        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]
            
            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in G[c1]:
                        G[c1].add(c2)
                        indegrees[c2] += 1
                    break
            else:
                if len(word1) > len(word2):
                    return ""
        
        # Build Q
        Q = deque([c for c, v in indegrees.items() if not v])
        
        res = []
        while Q:
            letter = Q.popleft()
            res.append(letter)
            
            for nei in G[letter]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    Q.append(nei)
                    
        return "".join(res) if len(res) == len(indegrees) else ""           
            
            