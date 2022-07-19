class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
                
        for row in range(1, numRows + 1):
            cur_row = [1] * row
            
            for i in range(1, row - 1):
                cur_row[i] = res[-1][i-1] + res[-1][i]
            
            res.append(cur_row)
        
        return res
                     
            