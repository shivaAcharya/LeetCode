class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        car = [(p, s) for p, s in zip(position, speed)]
        stack = []
        
        for pos, spd in reversed(sorted(car)):
            stack.append((target - pos) / spd)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()    
        
        return len(stack)
    
    """
    target = 100
    psition = [0, 2. 4]
    speed = [4, 2, 1]
    car = [(0, 4), (2, 2), (4, 1)]
                      ^
                             ~25
    stack = [<25, ]
    
    
    """
    