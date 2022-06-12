class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:

        tax = 0      
        i = 0
        while income and i < len(brackets):
            diff = brackets[i][0] - brackets[i-1][0] if i > 0 else brackets[i][0]
            if income < diff:
                tax += round(income * brackets[i][1] * 0.01, 5)
                break
            tax += round(diff * brackets[i][1] * 0.01, 5)
            income -= diff
            i += 1
        
        return tax