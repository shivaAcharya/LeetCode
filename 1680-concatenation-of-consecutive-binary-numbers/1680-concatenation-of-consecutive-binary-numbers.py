class Solution:
    def concatenatedBinary(self, n: int) -> int:
        # Simulation
        
        bin_str_lst = []
        
        for i in range(1, n + 1):
            bin_str_lst.append(bin(i)[2:])
        
        return int("".join(bin_str_lst), 2) % (10**9 + 7)