# class TrieNode:
    
#     def __init__(self):
#         self.children = {}
#         self.count = 0
        

# class Trie:
    
#     def __init__(self):
#         self.root = TrieNode()
        
    
#     def insert(self, word):
#         cur = self.root
        
#         for c in word:
#             if c not in cur.children:
#                 cur.children[c] = TrieNode()
            
#             cur = cur.children[c]
#             cur.count += 1
    
    
#     def count(self, word):
#         res = 0
#         cur = self.root
#         for c in word:
#             if c in cur.children:
#                 cur = cur.children[c]
#                 res += cur.count

#         return res



class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        
#         trie = Trie()
        
#         for word in words:
#             trie.insert(word)
        
#         # return [trie.count(word) for word in words]
        
#         return map(trie.count, words)
        pre_freq = Counter()
        res = []
        
        for word in words:
            for i in range(len(word)):
                pre_freq[word[:i + 1]] += 1
        
        for word in words:
            score = 0
            for i in range(len(word)):
                if word[:i + 1] not in pre_freq:
                    break
                score += pre_freq[word[:i + 1]]
            
            res.append(score)
            
        return res