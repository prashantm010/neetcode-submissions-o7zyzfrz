class Solution {
    private void dfs(int[][] height,int x, int y, int rows, int cols, boolean[][] visits, int prevHeight) {
        if (x < 0 || y < 0 || x >= rows || y >= cols || visits[x][y] || prevHeight > height[x][y]) {
            return;
        }
        visits[x][y] = true;
        dfs(height,x-1,y,rows,cols,visits,height[x][y]);
        dfs(height,x,y-1,rows,cols,visits,height[x][y]);
        dfs(height,x+1,y,rows,cols,visits,height[x][y]);
        dfs(height,x,y+1,rows,cols,visits,height[x][y]);
    }

    public List<List<Integer>> pacificAtlantic(int[][] heights) {
        int rows = heights.length;
        int cols = heights[0].length;

        boolean[][] pac = new boolean[rows][cols];
        boolean[][] atl = new boolean[rows][cols];

        for (int c = 0; c < cols; c++) {
            dfs(heights,0, c, rows, cols, pac, heights[0][c]);
            dfs(heights,rows-1, c, rows, cols, atl, heights[rows-1][c]);
        }

        for (int r = 0; r < rows; r++) {
            dfs(heights,r, 0, rows, cols, pac, heights[r][0]);
            dfs(heights,r, cols-1, rows, cols, atl, heights[r][cols-1]);
        }

        List<List<Integer>> res = new ArrayList<>();
        for (int x=0; x<rows; x++) {
            for (int y=0; y<cols; y++) {
                if (pac[x][y] && atl[x][y]) {
                    res.add(Arrays.asList(x,y));
                }
            }
        }
        return res;
    }
}
