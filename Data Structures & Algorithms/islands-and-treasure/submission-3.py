class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visits = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or ((r,c)) in visits or grid[r][c] == -1:
                return

            visits.add((r,c))
            q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    visits.add((r,c))
                    q.append((r,c))

        dist = 0
        while q:
            n = len(q)
            for i in range(n):
                pos = q.popleft()
                x = pos[0]
                y = pos[1]
                grid[x][y] = dist
                dfs(x-1, y)
                dfs(x, y-1)
                dfs(x+1, y)
                dfs(x, y+1)
            dist += 1
        