class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key=lambda x : -x[1])
        res = 0
        
        for num, units in boxTypes:
            
            if num > truckSize:
                res += truckSize * units
                break
            
            res += num * units
            truckSize -= num
        
        return res
            
            