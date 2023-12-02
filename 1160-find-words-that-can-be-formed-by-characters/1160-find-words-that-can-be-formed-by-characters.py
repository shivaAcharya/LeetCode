class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
                
        res = 0
        
        for word in words:
            chars_counter = Counter(chars)
            for c in word:
                if chars_counter[c] == 0:
                    break
                chars_counter[c] -= 1
            else:
                res += len(word)
                
        return res
    