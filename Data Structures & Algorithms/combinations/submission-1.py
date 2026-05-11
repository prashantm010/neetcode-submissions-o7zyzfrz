class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(index, count, currSet):
            if count == 0:
                res.append(currSet.copy())
                return

            if count < 0:
                return

            for i in range(index, n + 1):
                currSet.append(i)
                dfs(i + 1, count - 1, currSet)
                currSet.pop()

        dfs(1, k, [])
        return res
