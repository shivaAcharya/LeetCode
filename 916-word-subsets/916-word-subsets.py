class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        counter_words2 = defaultdict(int)
        for word in B:
            word_counter = Counter(word)
            for k, v in word_counter.items():
                if v > counter_words2[k]:
                    counter_words2[k] = v

        res = []

        for word in A:
            counter_word = Counter(word)

            if all(v <= counter_word[k] for (k, v) in counter_words2.items()):
                res.append(word)
        
        return res

            