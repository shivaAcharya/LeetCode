class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1, counter2 = Counter(nums1), Counter(nums2)
        
        res = []
        
        for num, freq in counter1.items():
            if num in counter2:
                res.extend([num] * min(freq, counter2[num]))
        
        return res
        