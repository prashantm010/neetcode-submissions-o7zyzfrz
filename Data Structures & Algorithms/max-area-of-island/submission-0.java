class Solution {
    public int maxAreaOfIsland(int[][] grid) {
        Set<String> visits = new HashSet<>();
        int area = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                area = Math.max(area, dfs(grid, visits, i, j));
            }
        }
        return area;
    }

    private int dfs(int[][] grid, Set<String> visits, int i, int j) {
        if (i < 0 || j < 0 || i >= grid.length || j >= grid[0].length || grid[i][j] == 0
                || visits.contains(i + "," + j)) {
            return 0;
        }

        visits.add(i + "," + j);
        return 1 + dfs(grid, visits, i + 1, j) + dfs(grid, visits, i, j + 1) + dfs(grid, visits, i - 1, j)
                + dfs(grid, visits, i, j - 1);
    }
}
