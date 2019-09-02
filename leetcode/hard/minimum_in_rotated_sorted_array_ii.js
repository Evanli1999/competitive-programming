//https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/description/

/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    let left = 0;
    let right = nums.length-1;
    let middle = Math.floor((left+right)/2);
    let tempmin = nums[left];
    let res;
    let temp;
    
    if(right === -1) {
        //console.log("right 0 or -1");
        return 0;
    }
    if(right === 0) {
        return nums[0];
    }
    
    while(right-left > 1) {
        //console.log("while loop" + left + " - " + right);
        if(nums[left] < nums[middle]) {
            left = middle;
            middle = Math.floor((left+right)/2);
            continue;
        }
        
        if(nums[left] > nums[middle]) {
            right = middle;
            middle = Math.floor((left+right)/2);
            continue;
        }
        
        temp = nums[left];
        while((left != middle) && (temp == nums[left])) {
            left++;
        }
        if(temp > nums[left]) {
            return nums[left];
        }
        middle = Math.floor((left+right)/2);
    }
    
    //console.log("exited: " + left + ' - ' + right);
    
    if(nums[left] < nums[left+1]) {
        res = nums[left];
    }
    res = nums[left+1];
    
    return (res < tempmin) ? res : tempmin;
};