'''
https://leetcode.com/problems/palindrome-pairs/solution/
'''

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def all_valid_prefixes(word):
            valid_prefixes = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    valid_prefixes.append(word[:i])
            return valid_prefixes

        def all_valid_suffixes(word):
            valid_suffixes = []
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    valid_suffixes.append(word[i + 1:])
            return valid_suffixes

        word_lookup = {word: i for i, word in enumerate(words)}
        solutions = []

        for word_index, word in enumerate(words):
            reversed_word = word[::-1]

            # Build solutions of case #1. This word will be word 1.
            if reversed_word in word_lookup and word_index != word_lookup[reversed_word]:
                solutions.append([word_index, word_lookup[reversed_word]])

            # Build solutions of case #2. This word will be word 2.
            for suffix in all_valid_suffixes(word):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_lookup:
                    solutions.append([word_lookup[reversed_suffix], word_index])

            # Build solutions of case #3. This word will be word 1.
            for prefix in all_valid_prefixes(word):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_lookup:
                    solutions.append([word_index, word_lookup[reversed_prefix]])
            
        return solutions
    '''
    Time Complexity => O(k^2 * n)
    Space Complexity => O((k + n)^2)    
    '''
                    