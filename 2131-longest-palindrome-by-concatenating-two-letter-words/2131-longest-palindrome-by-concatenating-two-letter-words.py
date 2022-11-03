class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        words_counter = Counter(words)
        central = False
        length = 0
        
        for word, count in words_counter.items():
            if word[0] != word[1]:
                length += min(count, words_counter[word[::-1]])
            else:
                if count % 2 == 0:
                    length += count
                else:
                    length += count - 1
                    central = True
                            
        
        if central:
            length += 1
        
        return length * 2
                
                
                