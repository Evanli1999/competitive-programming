class Solution:
    def recurr(self, num):
        if num in self.memo:
            return self.memo[num]
        sqrt = int(num**0.5)
        if sqrt**2 == num:
            ans = 0
        else:
            ans = False
            for i in range(sqrt, 0, -1):
                res = self.recurr(num - i**2)
                if res:
                    if ans:
                        ans = min(ans, res)
                    else:
                        ans = res
        self.memo[num] = ans+1
        return ans+1


    def numSquares(self, n: int) -> int:
        self.memo = {}
        return self.recurr(n)
