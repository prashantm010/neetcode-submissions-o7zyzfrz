class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cMap = dict()
        res = 0
        i = 0

        for j in range(len(s)):
            cMap[s[j]] = 1 + cMap.get(s[j], 0)

            while (j - i + 1) - max(cMap.values()) > k:
                cMap[s[i]] -= 1
                i += 1

            res = max(j - i + 1, res)

        return res
