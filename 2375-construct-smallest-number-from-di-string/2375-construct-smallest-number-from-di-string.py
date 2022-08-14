class Solution:
    def smallestNumber(self, pattern: str) -> str:
        
        res = []

        def backtrack(nums, i):
            if len(tmp) == len(pattern) + 1:
                res.append("".join([str(i) for i in tmp]))
                return

            for j, num in enumerate(nums):

                if num in tmp:
                    continue

                if pattern[i] == "I" and num < tmp[-1]:
                    continue

                if pattern[i] == "D" and num > tmp[-1]:
                    continue

                tmp.append(num)

                backtrack(nums[:j] + nums[j+1:], i+1)
                tmp.pop()                   


        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        for num in nums:
            tmp = [num]
            backtrack(nums, 0)

        return min(res)
    