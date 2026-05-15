class Solution:
    def totalNQueens(self, n: int) -> int:
        counter = 0
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            nonlocal counter
            if r == n:
                counter += 1
                return
            for c in range(n):
                if self.isSafe(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."

        backtrack(0)
        return counter

    def isSafe(self, row, col, board):
        r = row - 1
        while r >= 0:
            if board[r][col] == "Q":
                return False
            r -= 1

        r, c = row - 1, col - 1
        while r >= 0 and c >= 0:
            if board[r][c] == "Q":
                return False
            r = r - 1
            c = c - 1

        r, c = row - 1, col + 1
        while r >= 0 and c <= len(board) - 1:
            if board[r][c] == "Q":
                return False
            r = r - 1
            c = c + 1

        return True
