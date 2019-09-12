class Solution:
    def decodeAtIndex(self, s, k):
        print(k)

        tape_length = 0
        prev_char = None
        prev_word = ''

        for l in s:
            if 48 <= ord(l) <= 57:
                prev_length = tape_length
                tape_length *= (ord(l)-48)
                if tape_length == k:
                    return prev_char
                if tape_length > k:
                    if k % prev_length == 0:
                        return prev_char
                    return self.decodeAtIndex(s, k%prev_length)
            else:
                prev_char = l
                tape_length+=1
                if k == tape_length:
                    return l

s = Solution()
