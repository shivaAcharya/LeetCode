"""
s = A B A B       k = 2
    l
          r
    
res = 4
window = {
    A : 2,
    B : 2,
}


s = A A B A B B A     k = 1
      l
              r
    
res = 4
window = {
    A : 3,
    B : 3,
}

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        window = defaultdict(int)
        res = l = 0
        
        for r, c in enumerate(s):
            window[c] += 1
            
            while (r - l + 1) - max(window.values()) > k:
                window[s[l]] -= 1
                l += 1
            
            res = max(res, (r - l + 1))
        
        return res            
        