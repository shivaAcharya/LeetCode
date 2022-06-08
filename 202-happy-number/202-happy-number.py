class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()

        while n != 1 and n not in visited:
            visited.add(n)
            total = 0
            while n:
                total += (n % 10) ** 2
                n //= 10
            n = total                    

        return n == 1