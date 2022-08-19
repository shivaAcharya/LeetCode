'''
https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/2448243/Python-oror-Easily-Understood-oror-Faster-than-90-oror-Explanation
'''
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        	  
        subsequence = defaultdict(int)
        num_count = Counter(nums)

        for num in nums:
            if not num_count[num]:
                continue

            if subsequence[num - 1] > 0:
                subsequence[num - 1] -= 1
                subsequence[num] += 1
            else:
                if not num_count[num + 1] or not num_count[num + 2]:
                    return False
                num_count[num + 1] -= 1
                num_count[num + 2] -= 1
                subsequence[num + 2] += 1
            num_count[num] -= 1

        return True