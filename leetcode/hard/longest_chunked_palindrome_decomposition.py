class Solution:
    def greedy(self,i):
        if i == len(self.text)-i-1:
            return 1
        elif i > len(self.text)-i-1:
            return 0
        else:
            ans = 1
            initial = i
            while i < len(self.text)-i-1:
                while self.text[initial] != self.text[-i-1] and i < len(self.text)-i-1:
                    i+=1
                left = self.text[initial:i+1]
                right = self.text[-i-1:-initial] if initial else self.text[-i-1:]

                if i < len(self.text)-i-1 and left == right:
                    return 2 + self.greedy(i+1)
                i+=1
            return 1

    def longestDecomposition(self, text):
        self.text = text
        return self.greedy(0)
