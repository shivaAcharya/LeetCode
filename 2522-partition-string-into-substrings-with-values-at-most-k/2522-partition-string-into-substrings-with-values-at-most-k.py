class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        
        k_len = len(str(k))
        partitions = 0
        
        idx = 0
        
        while idx < len(s):
            
            partition = s[idx : idx + k_len]
            
            if len(partition) == 1 and int(partition) > k:
                return -1
            
            partitions += 1
            idx += k_len
            if int(partition) > k:
                idx -= 1
        
        return partitions