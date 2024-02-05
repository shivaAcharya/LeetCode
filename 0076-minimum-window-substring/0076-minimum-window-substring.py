"""
If len(t) > len(s): return ""
target = {
    A : 1
    B : 1
    C : 1
}
min_subtr = ""
s = "A D O B E C O D E B A N C", t = "ABC"
     l     r   
    cur_wind = {
        A : 1
        D : 1
        O : 1
    }

"""
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s): return ""
        
        target = Counter(t)
        cur_wind = Counter()
        res, need, res_len = (-1, -1), len(t), float("inf")
    
        left = have = 0
        for right, char in enumerate(s):
            cur_wind[char] += 1
            
            if char in target and cur_wind[char] <= target[char]:
                have += 1
            
            # Compare
            while need == have:
                if right - left + 1 < res_len:
                    res_len = right - left + 1
                    res = (left, right)
                    
                # Remove left
                cur_wind[s[left]] -= 1

                if s[left] in target and cur_wind[s[left]] < target[s[left]]:
                    have -= 1

                left += 1

        if res_len == float("inf"):
            return ""
        l, r = res
        return s[l : r + 1]
        