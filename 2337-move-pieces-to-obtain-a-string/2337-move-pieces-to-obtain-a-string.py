class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_idx, target_idx = [], []
        for i, letter in enumerate(start):
            if letter != "_":
                start_idx.append((letter, i))
                
                
        for i, letter in enumerate(target):
            if letter != "_":
                target_idx.append((letter, i))
        
        if len(start_idx) != len(target_idx): return False
        
        for s, t in zip(start_idx, target_idx):
            
            if s[0] != t[0]: return False
            
            if s[0] == "L" and s[1] < t[1]:
                return False
            
            if s[0] == "R" and s[1] > t[1]:
                return False
        
        return True