class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1 = ptr2 = 0
        L1, L2 = len(word1), len(word2)
        res = []
        while ptr1 < L1 and ptr2 < L2:
            res.append(word1[ptr1])
            res.append(word2[ptr2])
            ptr1 += 1
            ptr2 += 1
        
        if ptr1 < L1:
            return "".join(res) + word1[ptr1:]
        
        return "".join(res) + word2[ptr2:]