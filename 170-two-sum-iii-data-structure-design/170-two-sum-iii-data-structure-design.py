class TwoSum:

    def __init__(self):
        self.nums = Counter()

        
    def add(self, number: int) -> None:
        self.nums[number] += 1
        

    def find(self, value: int) -> bool:
        for num in self.nums:
            
            if value - num in self.nums:
                if num == value // 2 and self.nums[num] < 2:
                    continue
                return True
            
        return False
        


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)