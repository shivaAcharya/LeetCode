class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        word_list = list(word)
        
        for i, c in enumerate(word_list):
            if c == ch:
                return "".join(list(reversed(word_list[: i + 1])) + word_list[i + 1:])
        
        return word