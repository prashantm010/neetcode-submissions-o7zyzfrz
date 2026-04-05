class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character> rowSet = null;
        Set<Character> colSet = null;

        for (int i = 0; i < board.length; i++) {
            rowSet = new HashSet<>();
            colSet = new HashSet<>();

            for (int j = 0; j < board[i].length; j++) {
                char r = board[i][j];
                char c = board[j][i];
                if (r != '.') {
                    if (rowSet.contains(r)) {
                        return false;
                    }
                    rowSet.add(r);
                }

                if (c != '.') {
                    if (colSet.contains(c)) {
                        return false;
                    }
                    colSet.add(c);
                }
            }
        }

        for (int i = 0; i < board.length; i = i + 3) {
            for (int j = 0; j < board[i].length; j = j + 3) {
                if (!checkBlocks(board, i, j)) {
                    return false;
                }
            }
        }
        return true;
    }

    private boolean checkBlocks(char[][] board, int i, int j) {
        Set<Character> blockSet = new HashSet<>();
        for (int x = i; x < i  + 3; x++) {
            for (int y = j; y < j + 3; y++) {
                if (board[x][y] != '.') {
                    if (blockSet.contains(board[x][y])) {
                        return false;
                    }
                    blockSet.add(board[x][y]);
                }
            }
        }
        return true;
    }
}