class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        m, n = len(s1), len(s2)
        f1 = [0] * 26
        f2 = [0] * 26

        for c in s1:
            f1[ord(c) - ord("a")] += 1

        for j in range(n):
            f2[ord(s2[j]) - ord("a")] += 1
            if j >= m:
                f2[ord(s2[j - m]) - ord("a")] -= 1
            if f1 == f2:
                return True
        return False