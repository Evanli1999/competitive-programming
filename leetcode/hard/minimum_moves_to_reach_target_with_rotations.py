from math import inf

class Solution:
    def valid(self,i,j,d):
        return (0 <= i < self.h-d and 0 <= j < self.w-1+d and (not self.grid[i][j]) and (not self.grid[i+d][j+1-d]))

    def recur(self,i,j,d):
        if (i,j,d) in self.active:
            return inf
        if (i,j,d) in self.memo:
            return self.memo[(i,j,d)]
        self.active.add((i,j,d))

        min_moves = inf
        if (i,j,d) == (self.h-1, self.w-2,0):
            min_moves = -1
        else:
            if self.valid(i,j+1,d):
                min_moves = min(min_moves, self.recur(i,j+1,d))
            if self.valid(i+1,j,d):
                min_moves = min(min_moves, self.recur(i+1,j,d))
            if self.valid(i+1-d,j+d,d):
                min_moves = min(min_moves, self.recur(i,j,1-d))

        self.active.remove((i,j,d))
        self.memo[(i,j,d)] = min_moves+1
        return min_moves+1

    def minimumMoves(self, grid):
        self.active = set() # set of (i,j,d) that is being solved rn
        self.memo = {} #(i,j,d) -> num_moves
                # d = 0 -> horizontal, d = 1 -> vertical
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])

        ans = self.recur(0,0,0)
        return ans if ans != inf else -1



