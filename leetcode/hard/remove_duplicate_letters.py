class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {letter:pos for pos, letter in enumerate(s)}
        stacc = []
        stacc_sett = set()

		for i, letter in enumerate(s):
            if letter not in stacc_sett:
                while(stacc and letter < stacc[-1] and i < last[stacc[-1]]):
                    stacc_sett.remove(stacc.pop())
                stacc.append(letter)
                stacc_sett.add(letter)
        return "".join(stacc)
