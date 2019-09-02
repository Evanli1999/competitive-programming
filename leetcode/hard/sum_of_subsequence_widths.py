# https://leetcode.com/problems/sum-of-subsequence-widths/submissions/

class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        MOD_VAL = 10**9 + 7
        n = len(A)
        A.sort()

        two_cache = [1]
        for i in range(1,n):
            two_cache.append((2 * two_cache[i-1]) % MOD_VAL)

        total_width = 0

        for i in range(0, n):
            total_width = (total_width % MOD_VAL) + ((two_cache[i] - two_cache[n-1-i]) * A[i]) % MOD_VAL

        return total_width % MOD_VAL
