# https://leetcode.com/problems/first-missing-positive/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # "put the positive numbers in their place" (if a[i] = e, swap a[i], a[e]) one by onee
        # after this, a[0] == 1 iff 1 in array, a[1] == 2 iff 2 in array ... etc
        # first a[i] != i+1, i+1 is the missing positive number

        length = len(nums)
        for i in range(length):
            curr = nums[i]
            while(curr > 0 and curr <= length and curr != nums[curr-1]):
                nums[i], nums[curr-1] = nums[curr-1], nums[i]
                curr = nums[i]

        for i, num in enumerate(nums):
            if num != i+1:
                return i+1
        return length+1
