class Solution:
    def combinationSum2(self, nums: List[int], target: int):
        res = []
        nums.sort()

        def dfs(index, total, currSet):
            if total < 0:
                return
            if total == 0:
                res.append(currSet.copy())
                return

            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue

                currSet.append(nums[i])  # DO
                dfs(i + 1, total - nums[i], currSet)  # EXPLORE
                currSet.pop()  # UNDO

        dfs(0, target, [])
        return res
