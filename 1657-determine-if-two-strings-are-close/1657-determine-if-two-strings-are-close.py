class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counter1, counter2 = Counter(word1), Counter(word2)
        
        return sorted(counter1.values()) == sorted(counter2.values()) and counter1.keys() == counter2.keys()