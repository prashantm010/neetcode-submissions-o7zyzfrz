class Solution:

    def mark_current_island(self, grid, i, j, m, n):
        if (i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != '1'):
            return
        grid[i][j] = '2'
        self.mark_current_island(grid, i-1, j, m, n)
        self.mark_current_island(grid, i, j-1, m, n)
        self.mark_current_island(grid, i+1, j, m, n)
        self.mark_current_island(grid, i, j+1, m, n)


    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        visited = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    self.mark_current_island(grid, i, j, m, n)
                    count += 1

        return count
        