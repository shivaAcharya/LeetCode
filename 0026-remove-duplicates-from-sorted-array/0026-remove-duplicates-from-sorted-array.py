class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        write_idx = 1

        for i in range(1, len(A)):
            if A[i] != A[i - 1]:
                A[write_idx] = A[i]
                write_idx += 1

        return write_idx
    