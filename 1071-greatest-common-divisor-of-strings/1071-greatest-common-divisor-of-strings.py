class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        prefix_str = ""
        
        for i in range(len(str2)):
            sub_str = str2[:i + 1]
            if not "".join(str1.split(sub_str)) and not "".join(str2.split(sub_str)):
                prefix_str = sub_str
        
        return prefix_str