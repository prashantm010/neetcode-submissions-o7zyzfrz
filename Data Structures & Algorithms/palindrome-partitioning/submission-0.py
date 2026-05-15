class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if self.isPalli(i, j, s):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPalli(self, i, j, s):
        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True
