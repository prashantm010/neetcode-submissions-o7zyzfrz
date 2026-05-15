class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        curr = []
        wordSet = set(wordDict)

        def dfs(i):
            if i == len(s):
                res.append(" ".join(curr))
                return

            for j in range(i, len(s)):
                word = s[i : j + 1]
                if word in wordSet:
                    curr.append(word)
                    dfs(j + 1)
                    curr.pop()

        dfs(0)
        return res
