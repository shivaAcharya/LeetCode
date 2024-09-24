class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        shift = 0
        res = [''] * len(shifts)
        i = len(shifts) - 1

        while i >= 0:
            shift += shifts[i]
            final_pos = (ord(s[i]) - ord('a') + shift) % 26
            print(final_pos)
            res[i] = chr(final_pos + ord('a'))
            i -= 1

        return "".join(res)
