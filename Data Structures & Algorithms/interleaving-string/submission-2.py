class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        dp = dict()
        return self.solve(s1, s2, s3, 0, 0, dp)

    def solve(self, s1, s2, s3, i, j, dp):
        if i == len(s1) and j == len(s2):
            return (i + j) == len(s3)

        if (i, j) in dp:
            return dp[(i, j)]

        res = False
        if i < len(s1) and (i + j) < len(s3) and s1[i] == s3[i + j]:
            res |= self.solve(s1, s2, s3, i + 1, j, dp)
        if j < len(s2) and (i + j) < len(s3) and s2[j] == s3[i + j]:
            res |= self.solve(s1, s2, s3, i, j + 1, dp)

        dp[(i, j)] = res
        return dp[(i, j)]
