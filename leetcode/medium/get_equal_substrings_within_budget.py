class Solution:
    def equalSubstring(self, s, t, maxCost):
        running_diff = 0
        last = -1
        best_substring_length = 0

        while last+1 < len(s) and running_diff <= maxCost - abs(ord(s[last+1]) - ord(t[last+1])):
            running_diff += abs(ord(s[last+1]) - ord(t[last+1]))
            last+=1
        best_substring_length = last+1

        for first in range(1, len(s)):
            running_diff -= abs(ord(s[first-1]) - ord(t[first-1]))

            while last+1 < len(s) and running_diff <= maxCost - abs(ord(s[last+1]) - ord(t[last+1])):
                running_diff += abs(ord(s[last+1]) - ord(t[last+1]))
                last += 1

            best_substring_length = max(best_substring_length, last-first+1)
        return best_substring_length

s = "abcd"
t = "cdef"
maxCost = 2
sol = Solution()
print(sol.equalSubstring(s, t, maxCost))

