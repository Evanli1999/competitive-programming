class Solution:
    def removeDuplicates(self, s, k):
        stack = []
        prev_letter = s[0]
        prev_count = 0

        for l in s:
            if l == prev_letter:
                prev_count += 1

            else:
                if prev_count:
                    stack.append((prev_letter, prev_count))
                    prev_letter, prev_count = l, 1
                elif not len(stack) or l != stack[-1][0]:
                    prev_letter, prev_count = l, 1
                else:
                    prev_letter, prev_count = stack.pop()
                    prev_count += 1

            if prev_count == k:
                    prev_count = 0

        if prev_count:
            stack.append((prev_letter, prev_count))

        return ''.join([p[0]*p[1] for p in stack])
