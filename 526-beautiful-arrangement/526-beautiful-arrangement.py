from itertools import permutations
class Solution:
    def countArrangement(self, n: int) -> int:
        self.res =  0
        perm = []
        nums = [i for i in range(1, n+1)]
        
        def is_valid(nums):
            
            for i, num in enumerate(nums):
                if (i+1) % num and num % (i+1):
                    return False
            #self.res += 1
            return True
        
        def permutation(nums):
            if not is_valid(perm):
                return
            
            if len(perm) == n:
                if is_valid(perm):
                    self.res += 1  
                return 
            
            for i, cand in enumerate(nums):
                perm.append(cand)
                permutation(nums[:i] + nums[i+1:])
                perm.pop()
            
        permutation(nums)

        # for perm in permutations(nums):
        #     if is_valid(perm):
        #         self.res += 1
    
        return self.res