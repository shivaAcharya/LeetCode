"""
logs = ["d1/","d2/","./","d3/","../","d31/"]

folder_depth

"""
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        folder_depth = 0
        
        for log in logs:
            if log.startswith('..') and folder_depth > 0:
                folder_depth -= 1
            elif not log.startswith('.'):
                folder_depth += 1
        
        return folder_depth
    