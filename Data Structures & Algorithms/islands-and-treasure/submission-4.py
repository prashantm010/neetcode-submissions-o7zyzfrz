class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        r, c = len(grid), len(grid[0])

        q = deque()
        visits = set()
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    visits.add((i, j))
                    q.append((i, j))

        def iterateRows(a, b):
            if a < 0 or a >= r or b < 0 or b >= c or grid[a][b] == -1 or (a,b) in visits:
                return
            visits.add((a, b))
            q.append((a, b))

        d = 0
        while q:
            n = len(q)
            for i in range(n):
                a, b = q.popleft()
                grid[a][b] = d
                iterateRows(a-1, b)
                iterateRows(a, b-1)
                iterateRows(a+1, b)
                iterateRows(a, b+1)
            d = d + 1
                    