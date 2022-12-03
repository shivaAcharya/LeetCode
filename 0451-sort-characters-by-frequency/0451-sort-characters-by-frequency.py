class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        keys = [k * v for k, v in counter.items()]

        keys.sort(key=lambda x:-len(x))
        
        return "".join(keys)