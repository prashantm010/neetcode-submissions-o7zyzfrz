class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [0] * n
        dp[0] = 0
        dp[1] = max(prices[1] - prices[0], 0)

        for i in range(2, n):
            dp[i] = dp[i - 1]
            for j in range(i):
                today = prices[i] - prices[j]
                prev = dp[j - 2] if j >= 2 else 0

                dp[i] = max(dp[i], today + prev)

        return dp[n - 1]
