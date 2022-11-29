import random
class RandomizedSet:

    def __init__(self):
        self.randomized_set = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.randomized_set:
            return False
        self.list.append(val)
        self.randomized_set[val] = len(self.list) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomized_set:
            return False
        
        idx = self.randomized_set.pop(val)
        last_item = self.list.pop()
        
        if idx != len(self.list):
            self.list[idx] = last_item
            self.randomized_set[last_item] = idx
        
        return True

    def getRandom(self) -> int:
        
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()