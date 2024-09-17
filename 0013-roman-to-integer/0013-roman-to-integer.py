class Solution:
    def romanToInt(self, s: str) -> int:
        rom_to_int = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000,
        }

        res = 0

        for i, rom in enumerate(s):
            if i != len(s) - 1:
                if rom == 'I' and (s[i + 1] == 'V' or s[i + 1] == 'X'):
                    res -= rom_to_int[rom]
                elif rom == 'X' and (s[i + 1] == 'L' or s[i + 1] == 'C'):
                    res -= rom_to_int[rom]
                elif rom == 'C' and (s[i + 1] == 'D' or s[i + 1] == 'M'):
                    res -= rom_to_int[rom]
                else:
                    res += rom_to_int[rom]
            else:
                res += rom_to_int[rom]
        return res
    