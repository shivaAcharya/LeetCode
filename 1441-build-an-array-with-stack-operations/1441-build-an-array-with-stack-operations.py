class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        
        target_set = set(target)
        stack = []
        res = []
        
        for i in range(1, n + 1):
            if i not in target_set:
                res.append("Push")
                res.append("Pop")
            else:
                stack.append(i)
                res.append("Push")
            
            if stack == target:
                break
        
        return res