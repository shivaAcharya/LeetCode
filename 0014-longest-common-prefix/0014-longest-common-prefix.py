class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res = strs[0]

        for s in strs[1:]:
            # If s < res, update res to s
            if len(s) < len(res):
                res = res[:len(s)]
            for i, c in enumerate(s):
                if i == len(res) or res[i] != c:
                    res = res[:i]
                    break

        return "".join(res)