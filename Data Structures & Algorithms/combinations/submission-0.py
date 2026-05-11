class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [i for i in range(1, n+1)]
        res = []


        def dfs(index, count, currSet):
            if count == 0:
                res.append(currSet.copy())
                return
            
            if count < 0:
                return

            for i in range(index, len(nums)):
                currSet.append(nums[i])
                dfs(i + 1, count-1, currSet)
                currSet.pop()

        dfs(0, k, [])
        return res
            

