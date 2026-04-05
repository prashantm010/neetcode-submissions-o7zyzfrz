class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])

        q = deque()
        visits = set()
        fresh = 0
        time = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    fresh = fresh + 1
                if grid[i][j] == 2:
                    q.append((i, j))

        def iterateRows(a, b):
            nonlocal fresh
            if a < 0 or a >= r or b < 0 or b >= c or grid[a][b] != 1:
                return
            grid[a][b] = 2
            q.append((a,b))
            fresh = fresh - 1

        while q and fresh > 0:
            n = len(q)
            for x in range(n):
                a, b = q.popleft()
                iterateRows(a-1, b)
                iterateRows(a, b-1)
                iterateRows(a+1, b)
                iterateRows(a, b+1)
                
            time = time + 1
        return time if fresh == 0 else -1


        