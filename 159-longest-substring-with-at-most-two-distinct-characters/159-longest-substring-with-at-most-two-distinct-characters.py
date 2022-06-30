class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        freq_map = {}
        l = max_length = 0
        
        for r, c in enumerate(s):
            
            freq_map[c] = freq_map.get(c, 0) + 1
            
            while len(freq_map) > 2:
                left_char = s[l]
                freq_map[left_char] -= 1
                
                if not freq_map[left_char]:
                    del freq_map[left_char]
                
                l += 1
            
            max_length = max(max_length, r - l + 1)
        
        return max_length