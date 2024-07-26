public class Solution {
    public bool ContainsDuplicate(int[] nums) {
        HashSet<int> hashset = new HashSet<int>(nums);
        return nums.Length != hashset.Count;
    }
}
