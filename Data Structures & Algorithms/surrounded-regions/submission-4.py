class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def dfs(x, y):
            if x < 0 or y < 0 or x >= rows or y >= cols or board[x][y] != "O":
                return
            board[x][y] = "T"
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (
                    (r in [0, rows - 1]) or (c in [0, cols - 1])
                ):
                    dfs(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"
