/*
leftProduct = [1] * nums.Length
nums = [1, 2, 3, 4]
leftProduct = [1, 1, 2, 6]
rightProduct = [24, 12, 4, 1]

*/
public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int size = nums.Length;
        int[] leftProduct = new int[size];
        int[] rightProduct = new int[size];
        Array.Fill(leftProduct, 1);
        Array.Fill(rightProduct, 1);
        
        for (int i = 1; i < size; i++){
            leftProduct[i] = leftProduct[i - 1] * nums[i - 1];
            // Console.WriteLine(leftProduct[i]);
        }
        // Console.WriteLine(leftProduct);
        for (int i = size - 2; i >= 0; i--){
            int num = nums[i];
            rightProduct[i] = rightProduct[i + 1] * nums[i + 1];
        }
        
        int[] res = new int[size];
        for (int i = 0; i < size; i++){
            res[i] = leftProduct[i] * rightProduct[i];
        }
        
        return res;
        
    }
}