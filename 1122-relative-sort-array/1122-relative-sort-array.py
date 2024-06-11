"""
arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]

2 => 3
3 => 2
1 => 1
4 => 1
6 => 1
7 => 1
9 => 1
19 => 1

[2, 2, 2, 1, 4, 3, 3, 9, 6, ]

"""
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        arr1.sort()
        counter = Counter(arr1)
        res = []
        
        for num in arr2:
            res.extend([num] * counter[num])
            del counter[num]
        
        for k, v in counter.items():
            res.extend([k] * v)
        
        return res
                
    