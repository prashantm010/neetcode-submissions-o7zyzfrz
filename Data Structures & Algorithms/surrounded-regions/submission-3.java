class Solution {
    private void dfs(char[][] board, int r, int c, int rows, int cols) {
        // Base case: out of bounds or not 'O'
        if (r < 0 || c < 0 || r >= rows || c >= cols || board[r][c] != 'O') {
            return;
        }
        // Mark the current cell as 'T' to indicate it's connected to a border
        board[r][c] = 'T';

        // Perform DFS in all four directions
        dfs(board, r-1, c, rows, cols); // up
        dfs(board, r+1, c, rows, cols); // down
        dfs(board, r, c-1, rows, cols); // left
        dfs(board, r, c+1, rows, cols); // right
    }

    public void solve(char[][] board) {
        if (board == null || board.length == 0 || board[0].length == 0) {
            return; // Handle edge case of an empty board
        }

        int rows = board.length;
        int cols = board[0].length;

        // Step 1: Perform DFS on the borders to mark all 'O's connected to the border as 'T'
        for (int r = 0; r < rows; r++) {
            // Check first and last column (borders)
            if (board[r][0] == 'O') {
                dfs(board, r, 0, rows, cols);
            }
            if (board[r][cols - 1] == 'O') {
                dfs(board, r, cols - 1, rows, cols);
            }
        }

        for (int c = 0; c < cols; c++) {
            // Check first and last row (borders)
            if (board[0][c] == 'O') {
                dfs(board, 0, c, rows, cols);
            }
            if (board[rows - 1][c] == 'O') {
                dfs(board, rows - 1, c, rows, cols);
            }
        }

        // Step 2: Modify the board:
        // All remaining 'O's are surrounded by 'X's, so change them to 'X'
        // All 'T's (which were originally 'O's connected to borders) revert back to 'O'
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (board[r][c] == 'O') {
                    board[r][c] = 'X'; // Surrounded 'O's become 'X'
                } else if (board[r][c] == 'T') {
                    board[r][c] = 'O'; // Border-connected 'O's revert to 'O'
                }
            }
        }
    }
}
