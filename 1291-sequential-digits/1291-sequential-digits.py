class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        #[low = 1000, high = 13000]
        numbers = "123456789"
        res = []
        n = 10
        
        for length in range(len(str(low)), len(str(high)) + 1): #[4, 5]
            for start in range(n - length): #[0, 5]
                num = int(numbers[start: start + length])
                if low <= num <= high:
                    res.append(num)
        
        return res
                