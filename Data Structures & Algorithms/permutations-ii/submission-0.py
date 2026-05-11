class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        visited = [False] * len(nums)

        def dfs(index, size, curr):
            if size == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if visited[i]:
                    continue

                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue

                visited[i] = True
                curr.append(nums[i])
                dfs(i + 1, size + 1, curr)
                curr.pop()
                visited[i] = False

        dfs(0, 0, [])
        return res
