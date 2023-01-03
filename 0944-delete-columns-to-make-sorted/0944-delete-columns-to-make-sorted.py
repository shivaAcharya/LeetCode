class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        
        columns = 0
        for i in range(len(strs[0])):
            last_char = ""
            for j in range(len(strs)):
                char = strs[j][i]
                if last_char and last_char > char:
                    columns += 1
                    break
                last_char = char
                
        return columns    