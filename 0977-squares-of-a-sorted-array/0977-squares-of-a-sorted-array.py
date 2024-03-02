class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        Find the pivot point
        Use two pointer technique to create res
        """
              
        r = 0
        while r < len(nums):
            if nums[r] >= 0:
                break
            r += 1
        
        # For all negative numbers
        if r == 0:
            return [num * num for num in nums]
        
        # For all positive numbers
        if r == len(nums):
            return [num * num for num in reversed(nums)]
            
        l = r - 1
        res = []
        while l >= 0 or r < len(nums):
            # print(f"l : {l}, r : {r}")
            sqr1 = nums[l] * nums[l] if l >= 0 else None
            sqr2 = nums[r] * nums[r] if r < len(nums) else None
            # print(f"sqr1 : {sqr1}, sqr2 : {sqr2}")
              
            if sqr1 is not None and sqr2 is not None:
                if sqr1 < sqr2:
                    res.append(sqr1)
                    l -= 1
                else:
                    res.append(sqr2)
                    r += 1
            elif sqr1:
                res.append(sqr1)
                l -= 1
            else:
                res.append(sqr2)
                r += 1
            
            # print(f"res : {res}")
            # print(f"l : {l}, r : {r}")

            
        return res
    