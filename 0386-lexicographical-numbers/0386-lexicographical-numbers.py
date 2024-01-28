class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        
        arr = []
        
        for i in range(1, n + 1):
            arr.append(str(i))
            
        arr.sort()
        
        arr = [int(n) for n in arr]
        return arr
        