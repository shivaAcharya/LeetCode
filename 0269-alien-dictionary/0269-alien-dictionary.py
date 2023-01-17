class Solution:
    def alienOrder(self, words: List[str]) -> str:
        G = defaultdict(set)
        indegrees = Counter({c : 0 for word in words for c in word})

        # Build G
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
        
        Q = deque([k for k, v in indegrees.items() if v == 0])
        
        new_word = []
        while Q:
            c = Q.popleft()
            new_word.append(c)

            for nei in G[c]:
                indegrees[nei] -= 1
                if indegrees[nei] == 0:
                    Q.append(nei)
            
        
        return "".join(new_word) if len(new_word) == len(indegrees) else ""