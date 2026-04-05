class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        area = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or ((r,c)) in visit or grid[r][c] != 1:
                return 0
            visit.add((r,c))
            a = 1 + dfs(r-1, c) + dfs(r, c-1) + dfs(r+1, c) + dfs(r, c+1)
            return a



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = max(area, dfs(r, c))

        return area
        