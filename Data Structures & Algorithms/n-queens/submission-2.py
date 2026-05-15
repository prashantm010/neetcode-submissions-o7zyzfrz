class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["." for _ in range(n)] for x in range(n)]
        print(board)

        def backtrack(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            for c in range(n):
                if self.isSafe(r, c, board):
                    board[r][c] = 'Q'
                    backtrack(r + 1)
                    board[r][c] = '.'
        backtrack(0)
        return res


    def isSafe(self, row, col, board):
        r = row - 1
        while r >= 0:
            if board[r][col] == 'Q':
                return False
            r -= 1

        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == 'Q':
                return False
            r = r - 1
            c = c - 1
        
        r, c = row - 1, col + 1
        while r >= 0 and c <= len(board) - 1:
            if board[r][c] == 'Q':
                return False
            r = r - 1
            c = c + 1

        return True

