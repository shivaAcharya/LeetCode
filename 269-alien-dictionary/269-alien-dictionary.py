class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj_list = defaultdict(set)
        indegrees = Counter({c : 0 for word in words for c in word})
        #print(indegrees)
        
        
        for word1, word2 in zip(words, words[1:]):
            for c, d in zip(word1, word2):
                if c != d:
                    if d not in adj_list[c]:
                        adj_list[c].add(d)
                        indegrees[d] += 1
                    break
            else:
                if len(word2) < len(word1):
                    return ""
        
        
        res = []
        # Initialize Q with 0 indegrees letters        
        Q = deque([k for k, v in indegrees.items() if v == 0])
        
        
        while Q:
            node = Q.popleft()
            res.append(node)
            
            for nei in adj_list[node]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    Q.append(nei)
        
        return "".join(res) if len(res) == len(indegrees) else ""
                