"""
seats = [1, 4, 5, 9]
students = [1, 2, 3, 6]
res = 2 + 2 + 3 = 7

seats = [1, 3, 5]
students = [2, 4, 7]
res = 1 + 1 + 2

[2, 2, 6, 6]
[1, 2, 3, 6]
1 + 3

"""

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        
        seats.sort()
        students.sort()
        res = 0
        
        for seat, student in zip(seats, students):
            res += abs(seat - student)
        
        return res
        