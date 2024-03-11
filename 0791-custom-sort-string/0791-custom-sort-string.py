from functools import cmp_to_key
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        
        def compare(x, y):
            if x not in order and y not in order:
                return 0
            if x in order and y not in order:
                return -1
            if x not in order and y in order:
                return 1
            if order.index(x) < order.index(y):
                return -1
            return 1
                
        sorted_list = sorted(s, key=cmp_to_key(compare))
        return "".join(sorted_list)
        