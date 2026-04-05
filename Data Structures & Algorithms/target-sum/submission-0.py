class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mp = dict()
        return self.solve(nums, 0, 0, target, mp)

    def solve(self, nums, i, currentSum, target, mp):
        if (i, currentSum) in mp:
            return mp[(i, currentSum)]
        if i == len(nums):
            return 1 if currentSum == target else 0
        
        plus = self.solve(nums, i+1, currentSum + nums[i], target, mp)
        minus = self.solve(nums, i+1, currentSum - nums[i], target, mp)
        mp[(i, currentSum)] = plus + minus
        return mp[(i, currentSum)]
        