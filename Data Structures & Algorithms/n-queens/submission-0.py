class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["." for _ in range(n)] for _ in range(n)]
        result = []

        def isValid(r, c):
            # check upward
            for i in range(r - 1, -1, -1):
                if board[i][c] == "Q":
                    return False

            # check left diagonal
            for i, j in zip(range(r - 1, -1, -1), range(c - 1, -1, -1)):
                if board[i][j] == "Q":
                    return False

            # check right diagonal
            for i, j in zip(range(r - 1, -1, -1), range(c + 1, n)):
                if board[i][j] == "Q":
                    return False

            return True

        def solve(r):
            if r >= n:
                result.append(["".join(row) for row in board])
                return
            for c in range(n):
                if isValid(r, c):
                    board[r][c] = "Q"
                    solve(r + 1)
                    board[r][c] = "."

        solve(0)
        return result
