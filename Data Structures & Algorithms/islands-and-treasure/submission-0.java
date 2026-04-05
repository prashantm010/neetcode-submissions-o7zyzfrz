class Solution {

    private void iterateRooms(int[][] grid, int x, int y, int rows, int cols, Deque<int[]> q, Set<String> visits) {
        String edge = x + "," + y;
        if (x < 0 || y < 0 || x >= rows || y >= cols || grid[x][y] == -1 || visits.contains(edge)) {
            return;
        }
        visits.add(edge);
        q.addLast(new int[]{x, y});
    }

    public void islandsAndTreasure(int[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        Set<String> visits = new HashSet<>();
        Deque<int[]> q = new LinkedList<>();

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 0) {
                    visits.add(r + "," + c);
                    q.addLast(new int[]{r, c});
                }
            }
        }

        int dist = 0;
        while (!q.isEmpty()) {
            int size = q.size();
            for (int i = 0; i < size; i++) {
                int[] vertex = q.pollFirst();
                int x = vertex[0];
                int y = vertex[1];
                grid[x][y] = dist;
                iterateRooms(grid, x - 1, y, rows, cols, q, visits);
                iterateRooms(grid, x, y - 1, rows, cols, q, visits);
                iterateRooms(grid, x + 1, y, rows, cols, q, visits);
                iterateRooms(grid, x, y + 1, rows, cols, q, visits);
            }
            dist++;
        }
    }
}