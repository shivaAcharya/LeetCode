"""

7 -> 3

0. aaaa
     ^

res = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1

{a -> 4} # 1
res = 4 + aa + aa + aa + aaa + aaa + aaaa = 10
    L + l

0.1 assa 
{a -> 2, s -> 2} # 2
res = 4 + assa + ss = 6
      L + L // 2

1. racecar #7
    ^^
{r -> 2, a -> 2, c -> 2, e -> 1} #4
res = 7 + racecar + aceca + cec + 
    L + 1 
    
2. abracecarba #11
{a -> 4, b -> 2, r -> 2, c -> 2, e -> 1} #5
res = 11 + abracecarba + bracecarb + racecar + aceca + cec +  = 16
    L + L // 2


 r a c e c a r
 l           r
res = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1

"""
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = len(s)
        
        # Handle odd
        for i in range(res):
            l, r = i - 1, i + 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
        
        # Handle even
        for i in range(res):
            l, r = i, i + 1
            
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
    
        return res
    