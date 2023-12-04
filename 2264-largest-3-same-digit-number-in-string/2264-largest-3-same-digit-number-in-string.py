class Solution:
    def largestGoodInteger(self, num: str) -> str:
        
        max_good_integer = ""
        
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                if not max_good_integer or int(max_good_integer) < int(num[i : i + 3]):
                    max_good_integer = num[i : i + 3]
        
        return max_good_integer
    