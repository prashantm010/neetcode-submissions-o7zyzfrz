class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.solve(board, i, j, word, 0):
                    return True

        return False
        
    def solve(self, board, i, j, word, idx):
        if len(word) == idx:
            return True
        if (i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] == "$"):
            return False
        if (board[i][j] != word[idx]):
            return False
        temp = board[i][j]
        board[i][j] = "$"
        # Backtrack
        for i_, j_ in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
            x = i + i_
            y = j + j_
            if (self.solve(board, x, y, word, idx+1)):
                return True
        board[i][j] = temp


        