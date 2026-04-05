class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = dict()

        def solve(i, p):
            if i >= n:
                return 0
            if (i, p) in dp:
                return dp[(i,p)]

            take, skip = 0, 0
            if (p == -1 or nums[i] > nums[p]):
                take = 1 + solve(i+1, i)

            skip = solve(i+1, p)
            dp[(i,p)] = max(take, skip)
            return dp[(i,p)]

        return solve(0, -1)
        