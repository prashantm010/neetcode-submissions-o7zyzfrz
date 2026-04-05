class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return max(self.util(nums[1:]), self.util(nums[:-1]))

    def util(self, nums):
        n = len(nums)

        if n == 1:
            return nums[0]
        dp = [0] * (n + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n + 1):
            dp[i] = max(nums[i - 1] + dp[i - 2], dp[i - 1])

        return dp[n]
