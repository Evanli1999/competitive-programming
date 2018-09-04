//https://leetcode.com/problems/product-of-array-except-self/description/

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int [] result = new int[nums.length];
        
        int accum = 1;
        for (int i = 0; i < result.length; i++) {
            result[i] = accum;
            accum *= nums[i]; 
        } //i.e. result[i] is the product of all elements to it's left (1 at index 0)
        //O(n)
        
        accum = 1;
        for (int i = nums.length-1; i >= 0; i--) {
            result[i] *= accum;
            accum *= nums[i];
        } //note that accum will be the product of all element to num[i]'s right (starting at 1)
        //O(n)
        
        return result;
    }
}