#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#    Each row must contain the digits 1-9 without repetition.
#    Each column must contain the digits 1-9 without repetition.
#    Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#Note:
#
#    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#    Only the filled cells need to be validated according to the mentioned rules.

import collections
from collections import defaultdict
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Using defaultdict here because we need to initialize the values of the keys as sets
        # Otherwise we will have to check if the key is present in the dictionary or not
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)
        for r in range(len(board)):
            for c in range(len(board[r])):
                cur = board[r][c]
                box = (r//3,c//3)
                if cur == '.':
                    continue
                if ((cur in rows[r]) or (cur in cols[c]) or (cur in boxes[box])):
                    return False
                else:
                    rows[r].add(cur)
                    cols[c].add(cur)
                    boxes[box].add(cur)
        return True