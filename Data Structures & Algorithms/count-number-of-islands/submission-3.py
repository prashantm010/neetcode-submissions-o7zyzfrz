class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visits = set()

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1'):
                return
            grid[r][c] = 2
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r+1, c)
            dfs(r, c+1)

        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    dfs(r, c)
                    count += 1
        return count

        