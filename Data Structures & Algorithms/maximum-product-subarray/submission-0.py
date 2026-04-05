class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n, res = len(nums), nums[0]
        p = s = 0
        for i in range(n):
            p = nums[i] * (p or 1)
            s = nums[n - 1 - i] * (s or 1)
            res = max(res, max(p, s))
        return res
