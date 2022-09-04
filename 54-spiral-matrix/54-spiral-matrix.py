class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        top, bottom = 0, len(matrix)
        left, right = 0, len(matrix[0])

        while left < right and top < bottom:
            # Store all elem from top row
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # Store all elem from right col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # Check if out of bounds
            if not (left < right and top < bottom):
                break

            # Store all elem from bot row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # Store all elem from left col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res