class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        l = math.sqrt(len(nums))
        self.length = math.ceil(len(nums) / l)
        self.b = [0] * self.length
        for i in range(len(nums)):
            self.b[i // self.length] += nums[i]
            

    def update(self, i: int, val: int) -> None:
        b_l = i // self.length
        self.b[b_l] = self.b[b_l] - self.nums[i] + val
        self.nums[i] = val
        

    def sumRange(self, i: int, j: int) -> int:
        cur_sum = 0
        startBlock = i // self.length
        endBlock = j // self.length
        
        if startBlock == endBlock:
            for k in range(i, j + 1):
                cur_sum += self.nums[k]
        else:
            for k in range(i, (startBlock + 1) * self.length):
                cur_sum += self.nums[k]
            for k in range(startBlock + 1, endBlock):
                cur_sum += self.b[k]
            for k in range(endBlock * self.length, j + 1):
                cur_sum += self.nums[k]
        
        return cur_sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)