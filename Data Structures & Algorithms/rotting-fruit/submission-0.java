class Solution {
    public int orangesRotting(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        Deque<int[]> q = new LinkedList<>();

        int fresh = 0;
        int time = 0;
        
        for (int r=0;r<rows;r++) {
            for (int c=0;c<cols;c++) {
                if (grid[r][c] == 1) {
                    fresh++;
                }
                if (grid[r][c] == 2) {
                    q.addLast(new int[] {r,c});
                }
            }
        }
        
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        while (!q.isEmpty() && fresh > 0) {
            int size = q.size();
            for (int i=0; i<size; i++) {
                int[] node = q.pollFirst();
                int x = node[0];
                int y = node[1];
                for(int[] dir: directions) {
                    int row = x + dir[0];
                    int col = y + dir[1];

                    if (row < 0 || row >= rows || col < 0 || col >= cols || grid[row][col] != 1) {
                        continue;
                    }

                    grid[row][col] = 2;
                    q.add(new int[] {row, col});
                    fresh--;
                }
            }
            time++;
        }
        return fresh > 0 ? -1 : time;
    }
}
