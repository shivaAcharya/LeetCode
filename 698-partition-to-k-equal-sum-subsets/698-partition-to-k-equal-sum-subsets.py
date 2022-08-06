class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        
        total = sum(nums)
        if (total % k) != 0:
            return False
        
        target = total / k
        subset_sums = [0] * k
        
        # Optimization 2 for TLE
        nums.sort(reverse=True)
        
        def search(i: int) -> bool:
            if i == len(nums):
                return True
            
            for j in range(k):
                if subset_sums[j] + nums[i] <= target:
                    subset_sums[j] += nums[i]
                    if search(i+1):
                        return True
                    subset_sums[j] -= nums[i]
                    
                    # Optimization 1 for TLE
                    if subset_sums[j] == 0:
                        return False
                    
            return False
            
        return search(0)
        