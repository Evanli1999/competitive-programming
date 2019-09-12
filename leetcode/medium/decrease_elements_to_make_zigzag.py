class Solution:
    def decreaseEven(self):
        num_decrease = 0;
        for i in range(0, len(self.nums), 2):
            minAdj = self.nums[i]+1
            if i != 0:
                minAdj = min(minAdj, self.nums[i-1])
            if i != len(self.nums)-1:
                minAdj = min(minAdj, self.nums[i+1])
            if self.nums[i] >= minAdj:
                num_decrease += self.nums[i]-minAdj+1
        return num_decrease

    def decreaseOdd(self):
        num_decrease = 0;
        for i in range(1, len(self.nums), 2):
            minAdj = self.nums[i]+1
            if i != 0:
                minAdj = min(minAdj, self.nums[i-1])
            if i != len(self.nums)-1:
                minAdj = min(minAdj, self.nums[i+1])
            if self.nums[i] >= minAdj:
                num_decrease += self.nums[i]-minAdj+1
        return num_decrease

    def movesToMakeZigzag(self, nums) -> int:
        self.nums = nums
        return min(self.decreaseEven(), self.decreaseOdd())
