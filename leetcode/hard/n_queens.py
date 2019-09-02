# https://leetcode.com/problems/n-queens/

def locationsNextRow(size, queens):
        available_squares = set(range(0, size))
        row_num = len(queens) 
        for i, pos in enumerate(queens):
            if len(available_squares) == 0:
                return available_squares

            available_squares.discard(pos)
            available_squares.discard(pos + i - row_num)
            available_squares.discard(pos + row_num - i)

        return available_squares

def list2board(size, queens):
    return ["."*pos + "Q" + "."*(size-pos-1) for pos in queens]


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        queen_locations = [[x] for x in range(0, n)]

        for i in range(1,n): # adding all queens on row i
            queen_locations = [prev+[new_location] for prev in queen_locations for new_location in locationsNextRow(n, prev)]

        return [list2board(n, queens) for queens in queen_locations ]

