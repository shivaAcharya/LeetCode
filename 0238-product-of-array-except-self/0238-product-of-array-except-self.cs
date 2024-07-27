/*
nums = [1, 2, 3, 4]
leftProduct = [1, 1, 2, 6]
rightProduct = [24, 12, 4, 1]
res = [24, 12, 8, 6]
*/

public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int size = nums.Length;
        int[] leftProduct = new int[size];
        int[] rightProduct = new int[size];
        int[] res = new int[size];
        Array.Fill(leftProduct, 1);
        Array.Fill(rightProduct, 1);
        for (int i = 1; i < size; i++){
            leftProduct[i] = leftProduct[i - 1] * nums[i - 1];
        }        
        
        for (int i = size - 2; i >= 0; i--){
            rightProduct[i] = rightProduct[i + 1] * nums[i + 1];
        }
        
        for (int i = 0; i < size; i ++){
            res[i] = leftProduct[i] * rightProduct[i];
        }
        
        return res;
    }
}