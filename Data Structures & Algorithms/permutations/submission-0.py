class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(index, size, curr):
            if size == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if nums[i] in curr:
                    continue

                curr.append(nums[i])
                dfs(i + 1, size+1, curr)
                curr.pop()

        dfs(0, 0, [])
        return res
                
        