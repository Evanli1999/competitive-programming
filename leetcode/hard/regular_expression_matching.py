class Solution:
    def match(self, s_left, p_left) -> bool:
        if (s_left, p_left) in self.memo:
            return self.memo[(s_left, p_left)]

        if p_left == len(self.p):
            self.memo[(s_left, p_left)] = (s_left == len(self.s))
            return s_left == len(self.s)

        # match
        first = self.p[p_left]
        second = None
        if p_left + 1 < len(self.p):
            second = self.p[p_left + 1]

        if second != '*': # match single character
            if s_left == len(self.s):
                self.memo[(s_left, p_left)] = False
                return False

            if first == self.s[s_left] or first == '.':
                self.memo[(s_left, p_left)] = False
                return self.match(s_left+1, p_left+1)
            self.memo[(s_left, p_left)] = False
            return False

        else: # match 0+ characters
            while s_left <= len(self.s):
                if self.match(s_left, p_left + 2):
                    self.memo[(s_left, p_left)] = True
                    return True
                if s_left != len(self.s) and first != self.s[s_left] and first != '.':
                    break
                s_left+=1
            self.memo[(s_left, p_left)] = False
            return False

    def isMatch(self, s: str, p: str) -> bool:
        self.s = s
        self.p = p
        self.memo = {}

        return self.match(0,0)
