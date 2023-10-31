class Solution:
    def romanToInt(self, s: str) -> int:
        roman_to_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }
        
        running_sum = 0
        
        for i, rom in enumerate(s):
            if i < len(s) - 1 and roman_to_int[rom] < roman_to_int[s[i + 1]]:
                running_sum -= roman_to_int[rom]
            else:
                running_sum += roman_to_int[rom]
        
        return running_sum