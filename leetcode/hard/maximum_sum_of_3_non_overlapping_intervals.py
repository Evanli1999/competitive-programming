from collections import defaultdict

class Solution:
    def gt(self, trip1, trip2):
        if len(trip1) == 0:
            return False

        for n1, n2 in zip(trip1, trip2):
            if n1 > n2:
                return True
            if n1 < n2:
                return False
        return False

    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        sum_to_left = []
        sum_to_right = []

        total = 0
        for num in nums:
            sum_to_left.append(total)
            total+=num

        total = 0
        for num in nums[::-1]:
            sum_to_right.append(total)
            total+=num
        sum_to_right = sum_to_right[::-1]

        memo = defaultdict(lambda : ([], 0)) # start,number of arrs -> lex smallest positions of max sum, sum

        n = 3
        l = len(nums)
        for num_arrs in range(1,3+1):
            for i in range(l-num_arrs*k, -1, -1):
                locs_new, total_new = memo[(i+k, num_arrs-1)]
                locs_old, total_old = memo[(i+1, num_arrs)]

                candidate_total = total_new + total - sum_to_left[i] - sum_to_right[i+k-1]
                if candidate_total >= total_old:
                    memo[(i, num_arrs)] = ([i]+locs_new, candidate_total)
                else:
                    memo[(i, num_arrs)] = (locs_old, total_old)
        for k in memo:
            print(k, ':', memo[k])

        return memo[(0, k)][0]


