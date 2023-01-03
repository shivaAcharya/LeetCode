class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        columns = 0
        for i in range(len(strs[0])):
            last_char = ""
            for j in range(len(strs)):
                char = strs[j][i]
                if not last_char:
                    last_char = char
                elif last_char > char:
                    columns += 1
                    break
                last_char = char
                
        return columns    