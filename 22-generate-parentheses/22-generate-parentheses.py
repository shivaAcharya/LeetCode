class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        temp = []
        
        def helper(openCounter, closeCounter):
            # Base Case
            if closeCounter < openCounter:
                return
            
            if openCounter < 0 or closeCounter < 0:
                return
 
            if openCounter == 0 and closeCounter == 0:
                res.append("".join(temp))
                return
            
            # Recursive case
            temp.append("(")
            helper(openCounter - 1, closeCounter)
            temp.pop()
            
            temp.append(")")
            helper(openCounter, closeCounter - 1)
            temp.pop()
        
        helper(n, n)
        return res