class Solution:
    def minWindow(self, s: str, t: str) -> str:
        f1 = Counter(t)
        f2 = dict()
        res = ""
        resLen = float("inf")

        have = 0
        need = len(f1)
        i = 0

        for j in range(len(s)):
            c = s[j]
            f2[c] = 1 + f2.get(c, 0)

            if c in f1 and f2[c] == f1[c]:
                have += 1

            while have == need:
                if j - i + 1 < resLen:
                    res = s[i : j + 1]
                    resLen = j - i + 1
                f2[s[i]] -= 1

                if s[i] in f1 and f1[s[i]] > f2[s[i]]:
                    have -= 1

                i += 1

        return res
