class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        ptr1 = ptr2 = 0
        L1, L2 = len(nums1), len(nums2)
        
        while ptr1 < L1 and ptr2 < L2:
            if nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1
            else:
                return nums1[ptr1]
        
        return -1
    