class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        res = []
        tmp = [] # ['1', '2', '4']
        
        def backtrack():
            if len(tmp) == n:
                res.append(int("".join(tmp)))
                return
            
            for nei in range(10):
                if not tmp and nei == 0:
                    continue
                
                if not tmp or abs(int(tmp[-1]) - nei) == k:
                    tmp.append(str(nei))
                    backtrack()
                    tmp.pop()
        
        
        backtrack()
        return res