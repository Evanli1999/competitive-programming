class Solution:
    self.memo = None
    self.nums = None

    def recurr(available, current_side_length, sides_left, target_side_length):
        memo_key = (current_side_length, sides_left, available)

        # check memoized values first
        if self.memo.get(memo_key, False):
            return False

        if available == 0:
            if current_side_length == target_side_length and sides_left == 1:
                return True
            self.memo[memo_key] = False


        # we still have matches left to use
        int bitshift_position = 0;
        already_tried = [] # match lengths that we've tried already. We don't want to retry matches of the same length
        available_copy = available;
        while available > 0:
            # if the match hasn't been used yet, and match length has not been used yet, try to use it:
            if available%2 == 1 and nums[bitshift_position] not in already_tried:
                new_side_length = current_side_length + nums[bitshift_position]
                new_available = available_copy + 2**bitshift_position

                if new_side_length < target_side_length and recurr(new_available, new_side_length, sides_left, target_side_length):
                    return True
                if new_side_length == target_side_length and recurr(new_available, 0, sides_left1, target_side_length):
                    return True

        # trying every possible matchstick here has yielded false - the current configuration will definitely fail
        self.memo[memo_key] = False
        return False


    def makesquare(self, nums: List[int]) -> bool:
        self.memo = {} # maps (current_side_length, sides_left, available) -> bool (i.e. can or can not make square)
        self.nums = nums

        if sum(nums)%4 != 0:
            return False

        return recurr(2**len(nums)-1, 0, 4, sum(nums)/4)
