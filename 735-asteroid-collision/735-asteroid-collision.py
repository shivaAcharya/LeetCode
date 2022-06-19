class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        n = 0
        while n != len(asteroids):
            n = len(asteroids)
            new_asteroids = []
            
            i = 0
            while i < n:
                cur = asteroids[i]
                if i == n - 1:
                    new_asteroids.append(cur)
                    i += 1
                    continue
                nxt = asteroids[i+1]
                if cur < 0 and nxt < 0:
                    new_asteroids.append(cur)
                elif cur > 0 and nxt > 0:
                    new_asteroids.append(cur)
                elif cur < 0 and nxt > 0:
                    new_asteroids.append(cur)
                elif abs(cur) == abs(nxt):
                    i += 1
                elif abs(cur) > abs(nxt):
                    new_asteroids.append(cur)
                    i += 1
                else:
                    new_asteroids.append(nxt)
                    i += 1
                i += 1
            asteroids = new_asteroids
        
        return asteroids
                    
                