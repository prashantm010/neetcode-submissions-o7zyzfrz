class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        s1 = list(text1)
        s2 = list(text2)
        dp = [[-1 for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]

        def solve(i, j):
            if i >= len(s1) or j >= len(s2):
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            if s1[i] == s2[j]:
                return 1 + solve(i + 1, j + 1)

            dp[i][j] = max(solve(i + 1, j), solve(i, j + 1))
            return dp[i][j]

        return solve(0, 0)
