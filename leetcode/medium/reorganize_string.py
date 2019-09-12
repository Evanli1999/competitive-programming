from collections import Counter
from math import ceil

class Solution:
    def reorganizeString(self, s):
        n = len(s)

        # first check if it's even possible!
        count = Counter(s)
        for l in count:
            if count[l] > n-count[l]+1:
                return ""

        total = ""
        for l,c in count.most_common():
            total += l*c

        evens, odds = total[:ceil(n/2)], total[ceil(n/2):]

        ans = list(s)
        ans[::2] = evens
        ans[1::2] = odds

        return "".join(ans)
