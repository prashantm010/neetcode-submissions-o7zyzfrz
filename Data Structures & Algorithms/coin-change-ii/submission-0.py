class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n + 1)]

        def solve(i, amount):
            if amount == 0:
                return 1
            if i >= n:
                return 0
            if amount < coins[i]:
                return solve(i + 1, amount)

            if dp[i][amount] != -1:
                return dp[i][amount]

            take = solve(i, amount - coins[i])
            skip = solve(i + 1, amount)
            dp[i][amount] = take + skip
            return dp[i][amount]

        return solve(0, amount)
