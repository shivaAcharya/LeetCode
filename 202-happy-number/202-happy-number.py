class Solution:
    def isHappy(self, n: int) -> bool:
        str_n = str(n)
        visited = set([n])

        while str_n != "1":
            total = 0
            for digit in str_n:
                total += int(digit) ** 2
            if total in visited:
                return False
            visited.add(total)

            str_n = str(total)

        return True 