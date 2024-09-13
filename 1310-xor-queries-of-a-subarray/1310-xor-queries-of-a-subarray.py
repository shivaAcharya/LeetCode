# https://leetcode.com/problems/xor-queries-of-a-subarray/solution/
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        # Build prefix XOR array
        prefix_xor = [0] * (len(arr) + 1)
        for i in range(len(arr)):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        # Store the XOR result for each query in a variable
        result = [prefix_xor[r + 1] ^ prefix_xor[l] for l, r in queries]
        return result
    