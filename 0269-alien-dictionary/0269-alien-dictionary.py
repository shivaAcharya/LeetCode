'''
indegrees = {w:0, r:0, f:0, e:0, t:0}

Build graph

G = {
    t : {f},
    w : {e},
    r : {t},
    e : {r}
}

res = [w, e, r, t, f]
Q = []

return "".join(res) if len(res) == len(indegrees) else ""

'''

class Solution:
    def alienOrder(self, words: List[str]) -> str:

        indegrees = Counter({c : 0 for word in words for c in word})
        G = defaultdict(set)

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]

            for c1, c2 in zip(word1, word2):
                if c1 != c2:
                    if c2 not in G[c1]:
                        G[c1].add(c2)
                        indegrees[c2] += 1
                    break
            else:
                if len(word2) < len(word1):
                    return ""
        
        Q = deque([c for c, v in indegrees.items() if v == 0])
        res = []
        while Q:
            letter = Q.popleft()
            res.append(letter)

            for new_letter in G[letter]:
                indegrees[new_letter] -= 1
                if indegrees[new_letter] == 0:
                    Q.append(new_letter)
        
        return "".join(res) if len(res) == len(indegrees) else ""
"""
Time => O(E + V)   E is dependencies, V is total unique letters
Space => O(E + V)
"""