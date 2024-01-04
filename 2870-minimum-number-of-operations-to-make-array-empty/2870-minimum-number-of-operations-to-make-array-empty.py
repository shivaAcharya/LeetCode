class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        operations = 0

        for freq in counter.values():
            if freq == 1:
                return -1
            operations += (math.ceil(freq / 3))
        
        return operations
            