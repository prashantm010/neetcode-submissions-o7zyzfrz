class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            rowSet = set()
            colSet = set()
            for j in range(len(board[i])):
                r = board[i][j]
                c = board[j][i]
                if r != ".":
                    if r in rowSet:
                        return False
                    rowSet.add(r)
                if c != ".":
                    if c in colSet:
                        return False
                    colSet.add(c)

        for i in range(0, len(board), 3):
            for j in range(0, len(board[i]), 3):
                if not self.checkBlock(board, i, j):
                    return False

        return True

    def checkBlock(self, board, r, c):
        blockSet = set()
        for i in range(r, r + 3):
            for j in range(c, c + 3):
                if board[i][j] != ".":
                    if board[i][j] in blockSet:
                        return False
                    blockSet.add(board[i][j])
        return True
