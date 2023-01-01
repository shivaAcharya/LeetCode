class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s_list = s.split()
        mapping = {}
        mapped_word = set()
        idx = 0
        
        if len(pattern) != len(s_list): return False
        
        while idx < len(pattern):
            if pattern[idx] not in mapping:
                if s_list[idx] not in mapped_word:
                    mapping[pattern[idx]] = s_list[idx]
                    mapped_word.add(s_list[idx])
                else:
                    return False
            elif mapping[pattern[idx]] != s_list[idx]:
                return False
            idx += 1
        
        return True