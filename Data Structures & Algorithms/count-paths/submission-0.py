
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        def paths(i, j):
            if i >= m - 1 and j >= n - 1:
                return 1

            if i < 0 or i >= m or j < 0 or j >= n:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            right = paths(i, j + 1)
            down = paths(i + 1, j)
            
            dp[i][j] = right + down
            return dp[i][j]

        return paths(0, 0)
