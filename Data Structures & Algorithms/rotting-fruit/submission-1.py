
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        f = 0
        t = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    f += 1
                elif grid[r][c] == 2:
                    q.append((r, c))

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        while q and f > 0:
            s = len(q)
            for i in range(s):
                r, c = q.popleft()
                for dx, dy in directions:
                    x, y = r + dx, c + dy
                    if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x, y))
                        f -= 1
            t += 1

        return t if f == 0 else -1
