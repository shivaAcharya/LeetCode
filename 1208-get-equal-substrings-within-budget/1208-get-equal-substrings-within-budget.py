"""
s = abcd, t = bcdf, maxCost = 3

s --------> t

a - b + b - c + c - d => |a - d| => 3



s = abcd, t = cdef, maxCost = 3

a - c + b - d + c - e


"""


class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        N = len(s)
        
        max_len = 0
        # Starting index of the current substring
        start = 0
        # Cost of converting the current substring in s to t
        curr_cost = 0
        
        for i in range(N):
            # Add the current index to the substring
            curr_cost += abs(ord(s[i]) - ord(t[i]))
            
            # Remove the indices from the left end till the cost becomes less than the allowed
            while curr_cost > maxCost:
                curr_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            
            max_len = max(max_len, i - start + 1)
        
        return max_len