class SparseVector:
    def __init__(self, nums: List[int]):
        self.nums = {idx : v for idx, v in enumerate(nums) if v}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        res = 0
        
        for u, v in self.nums.items():
            if u in vec.nums:
                res += (v*vec.nums[u])            
        return res

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)