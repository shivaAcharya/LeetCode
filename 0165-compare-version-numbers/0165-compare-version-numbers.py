class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version_1 = version1.split(".")
        version_2 = version2.split(".")
        
        for i in range(max(len(version_1), len(version_2))):
            v1 = int(version_1[i]) if i < len(version_1) else 0
            v2 = int(version_2[i]) if i < len(version_2) else 0
            
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        
        return 0
    