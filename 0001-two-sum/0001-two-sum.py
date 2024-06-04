class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        for i, num in enumerate(nums):
            if num in hash_map:
                return [i, hash_map[num]]
            hash_map[target - num] = i
        