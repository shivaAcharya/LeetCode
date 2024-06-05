class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        char_count = Counter(words[0])
        
        for word in words:
            word_map = Counter(word)
            for c in char_count:
                if char_count[c] > word_map[c]:
                    char_count[c] = word_map[c]
        
        res = []
        for k, v in char_count.items():
            for _ in range(v):
                res.append(k)
                
        return res
        