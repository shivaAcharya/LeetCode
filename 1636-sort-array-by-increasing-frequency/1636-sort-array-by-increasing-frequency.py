class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        # def custom_comparator((k1, v1), (k2, v2)):
        #     if v2 > v1:
        #         return v2
        #     elif v2 < v1:
        #         return v1
        #     elif k1 > k2:
        #         return k1
        #     return k2
        return sorted(nums, key = lambda x : (counter[x], -x))
        