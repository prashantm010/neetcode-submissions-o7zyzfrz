class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        count = [0] * 128

        # Build frequency map
        for c in t:
            count[ord(c)] += 1

        i = 0
        min_len = float("inf")
        start = 0
        required = len(t)

        for j in range(len(s)):
            # Include character
            if count[ord(s[j])] > 0:
                required -= 1
            count[ord(s[j])] -= 1

            # Shrink window
            while required == 0:
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    start = i

                count[ord(s[i])] += 1
                if count[ord(s[i])] > 0:
                    required += 1
                i += 1

        return "" if min_len == float("inf") else s[start:start + min_len]