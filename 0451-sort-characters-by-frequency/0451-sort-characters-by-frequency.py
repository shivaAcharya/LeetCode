class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        
        freqs = sorted(counter.values(), reverse=True)
        
        res = []
        for freq in freqs:
            for c, frq in counter.items():
                if freq == frq:
                    res.append(c*frq)
                    del counter[c]
                    break
                    
        return "".join(res)        
        
        