class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = 0
        ans = 0
        cMap = dict()

        for j in range(len(s)):
            # Expand window by including s[j]
            cMap[s[j]] = 1 + cMap.get(s[j], 0)

            # ❗ While window is invalid, shrink from left
            while ((j - i + 1) - max(cMap.values()) > k):
                # (window size - count of most frequent char) > k
                # means we need more than k replacements → invalid window

                # Remove left character from window
                cMap[s[i]] -= 1

                # Move left pointer forward (shrink window)
                i += 1

            # Update answer with valid window size
            ans = max(ans, j - i + 1)

        return ans