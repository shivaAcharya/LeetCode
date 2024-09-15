class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.time_map[key]
        # Binary search        
        l, r = 0, len(values) - 1
        if not values or timestamp < values[l][0]:
            return ""
        
        while l < r:
            mid = (l + r) // 2
            
            if values[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid
        
        if values[l][0] > timestamp:
            return values[l - 1][1]
        
        return values[l][1] 
                
"""
      l
   m
       r
[1, 2, 4]

"""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)