class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        hash_map = defaultdict(int)
        ans = 0
        MOD = 10 ** 9 + 7
        
        def rev(x):
            res = []
            for c in reversed(str(x)):
                res.append(c)
                
            return int("".join(res))
        
        for num in nums:
            cur = num - rev(num)
            ans = (ans + hash_map[cur]) % MOD
            hash_map[cur] += 1
        
        return ans
    