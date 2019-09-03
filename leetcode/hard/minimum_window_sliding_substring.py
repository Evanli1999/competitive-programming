class Solution:
    def validateInterval(self, a, b):
        for letter in self.t_letter_count.keys():
            if self.letters_before_index[b+1].get(letter, 0) - self.letters_before_index[a].get(letter, 0) < self.t_letter_count[letter]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        cumulative_letter_count = {}

        letters_before_index = []
        for letter in s:
            letters_before_index.append(cumulative_letter_count.copy())
            if letter in cumulative_letter_count:
                cumulative_letter_count[letter] += 1
            else:
                cumulative_letter_count[letter] = 1

        letters_before_index.append(cumulative_letter_count.copy())

        # get number of characters in t:
        t_letter_count = {}
        for letter in t:
            if letter in t_letter_count:
                t_letter_count[letter] += 1
            else:
                t_letter_count[letter] = 1

        # chores
        self.letters_before_index = letters_before_index
        self.t_letter_count = t_letter_count
        a = 0
        b = min(len(s) - 1, len(t)-1)

        # find b_0
        while b < len(s) and not self.validateInterval(a,b):
            b+=1
        if b == len(s) and not self.validateInterval(a,b-1):
            return ""

        best_ab = (a,b)
        # increment a and and find b_a for each a in [0, len(s) - len(t)]
        while a <= len(s)-len(t):
            a+=1

            # find b_a
            while b < len(s) and not self.validateInterval(a,b):
                b+=1
            if b == len(s) and not self.validateInterval(a,b-1):
                return s[best_ab[0] : best_ab[1]+1]
            if b-a < best_ab[1] - best_ab[0]:
                best_ab = (a,b)

        return s[best_ab[0] : best_ab[1]+1]

S = "ab"
T = "aaab"
sol = Solution()
