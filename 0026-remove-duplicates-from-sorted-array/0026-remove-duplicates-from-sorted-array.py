class Solution:
    def removeDuplicates(self, A: List[int]) -> int:
        write_idx = 0

        for i in range(len(A)):
            if i < len(A) - 1 and A[i] == A[i + 1]:
                continue
            A[write_idx], A[i] = A[i], A[write_idx]
            write_idx += 1

        return write_idx