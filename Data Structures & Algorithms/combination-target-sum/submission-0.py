class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(index, total, currSet):
            if total == target:
                res.append(currSet.copy())
                return
            if total > target or index >= len(nums):
                return

            currSet.append(nums[index])
            dfs(index, total + nums[index], currSet)
            currSet.pop()
            dfs(index + 1, total, currSet)

        dfs(0, 0, [])
        return res
