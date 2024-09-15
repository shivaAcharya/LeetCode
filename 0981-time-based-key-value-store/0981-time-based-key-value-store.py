from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map[key]
        
        if not values or timestamp < values[0][1]:
            return ""
        
        l, r = 0, len(values) - 1
        
        while l < r:
            mid = (l + r) // 2
            
            if values[mid][1] < timestamp:
                l = mid + 1
            else:
                r = mid
        
        if values[l][1] > timestamp:
            return values[l - 1][0]
        
        return values[l][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)