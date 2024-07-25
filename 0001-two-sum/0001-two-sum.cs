public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        Dictionary<int, int> numIndex = new Dictionary<int, int>();
        
        for (int i = 0; i < nums.Length; i++){
            if (numIndex.ContainsKey(target - nums[i])){
                return [i, numIndex[target - nums[i]]];
            }
            if (!numIndex.ContainsKey(nums[i])){
                numIndex.Add(nums[i], i);
            }
        }
        return [-1, -1];
    }
}