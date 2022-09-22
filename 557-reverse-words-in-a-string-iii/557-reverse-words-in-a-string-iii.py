class Solution:
    def reverseWords(self, s: str) -> str:
#         s = s.split()
        
#         # Reverse each word
#         for i, word in enumerate(s):
#             tmp = []
            
#             for j in range(len(word) - 1, -1, -1):
#                 tmp.append(word[j])
            
#             s[i] = "".join(tmp)
        
#         return " ".join(s)
        
        res = []
        tmp = []
        
        for c in s:
            if c == " ":
                res.append("".join(reversed(tmp)))
                tmp = []
            else:
                tmp.append(c)
                
        res.append("".join(reversed(tmp)))
        
        return " ".join(res)