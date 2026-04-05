class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        dp = [[-1 for _ in range(2)] for _ in range(n + 1)]

        def solve(i, buy):
            if i >= n:
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]

            profit = 0
            if buy:
                take = solve(i + 1, False) - prices[i]
                not_take = solve(i + 1, True)
                profit = max(profit, take, not_take)
            else:
                sell = prices[i] + solve(i + 2, True)
                not_sell = solve(i + 1, False)
                profit = max(profit, sell, not_sell)

            dp[i][buy] = profit
            return dp[i][buy]

        return solve(0, True)