class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        
        # Reverse each word
        for i, word in enumerate(s):
            tmp = []
            
            for j in range(len(word) - 1, -1, -1):
                tmp.append(word[j])
            
            s[i] = "".join(tmp)
        
        return " ".join(s)