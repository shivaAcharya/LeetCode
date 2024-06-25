class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count_1 = students.count(1)
        count_0 = students.count(0)

        for sandwich in sandwiches:
            if sandwich == 1:
                if count_1 > 0:
                    count_1 -= 1
                else:
                    break
            elif count_0 > 0:
                count_0 -= 1
            else:
                break

        return count_0 + count_1
    