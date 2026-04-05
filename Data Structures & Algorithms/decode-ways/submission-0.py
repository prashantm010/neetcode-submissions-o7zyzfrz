class Solution:
    def numDecodings(self, s: str) -> int:
        arr = list(s)
        dp = [0] * (len(arr) + 1)
        dp[0] = 1
        dp[1] = 0 if int(arr[0]) == 0 else 1
        for i in range(2, len(arr) + 1):
            one = int("".join(arr[i - 1 : i]))
            two = int("".join(arr[i - 2 : i]))
            if one >= 1:
                dp[i] += dp[i - 1]

            if two >= 10 and two <= 26:
                dp[i] += dp[i - 2]
        return dp[len(s)]
