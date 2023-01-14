class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        hashmap = defaultdict(int)
        lcs = 0

        for num in nums:

            count, n = 0, num
            while n in nums_set:
                count += 1
                nums_set.remove(n)
                n -= 1
            
            count += hashmap[n]
            hashmap[num] = count
            lcs = max(lcs, count)
        
        return lcs