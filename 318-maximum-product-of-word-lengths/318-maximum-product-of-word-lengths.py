class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ########### INTUITIVE APPROACH ##################
        
        def have_common(word1, word2):
            word1 = set(word1)
            word2 = set(word2)
            for char in word2:
                if char in word1:
                    return True
            return False
        
        max_length = 0
        
        for i in range(len(words) - 1):
            for j in range(i+1, len(words)):
                if not have_common(words[i], words[j]):
                    max_length = max(max_length, len(words[i]) * len(words[j]))
        
        return max_length