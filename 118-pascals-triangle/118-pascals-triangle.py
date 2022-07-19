class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
                
        for row in range(2, numRows+1):
            cur_row = [1] * row
            
            for i in range(1, len(res[-1])):
                cur_row[i] = res[-1][i-1] + res[-1][i]
            
            res.append(cur_row)
        
        return res
                     
            