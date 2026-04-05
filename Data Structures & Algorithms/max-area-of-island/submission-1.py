class Solution:

    def dfs(self, grid, i, j, m, n, visited):
        edge = str(i) + "," + str(j)
        if (i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 or edge in visited):
            return 0
        visited.add(edge)
        return 1 + self.dfs(grid, i-1, j, m, n, visited) + self.dfs(grid, i, j-1, m, n, visited) + self.dfs(grid, i+1, j, m, n, visited) + self.dfs(grid, i, j+1, m, n, visited)
        

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        area = 0
        for i in range(m):
            for j in range(n):
                area = max(area, self.dfs(grid, i, j, m, n, visited))
        return area
        