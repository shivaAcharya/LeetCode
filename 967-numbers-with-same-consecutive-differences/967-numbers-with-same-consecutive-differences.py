class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        tmp = [] # ['1', '2', '4']
        
        def backtrack(i):
            if len(tmp) == n:
                res.append(int("".join(tmp)))
                return
            
            for nei in range(0, 10):
                if i == 0 and nei == 0:
                    continue
                
                if not tmp or abs(int(tmp[-1]) - nei) == k:
                    tmp.append(str(nei))
                
                    backtrack(i + 1)
                    tmp.pop()
        
        
        backtrack(0)
        return res