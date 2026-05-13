class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s, openCnt, closeCnt):
            if len(s) == 2 * n:
                res.append(s)
                return
            if openCnt < n:
                dfs(s + "(", openCnt + 1, closeCnt)
            if closeCnt < openCnt:
                dfs(s + ")", openCnt, closeCnt + 1)

        dfs("", 0, 0)
        return res
