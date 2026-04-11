class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # If s1 is longer, permutation can't exist
        if len(s1) > len(s2):
            return False

        m, n = len(s1), len(s2)

        # Frequency arrays for s1 and current window in s2
        f1 = [0] * 26
        f2 = [0] * 26

        # Build frequency map for s1
        for c in s1:
            f1[ord(c) - ord("a")] += 1

        # Sliding window over s2
        for j in range(n):
            # Add current character to window
            f2[ord(s2[j]) - ord("a")] += 1

            # ❗ Maintain window size = m
            if j >= m:
                # Remove character that goes out of window
                f2[ord(s2[j - m]) - ord("a")] -= 1

            # Check if current window is a permutation of s1
            if f1 == f2:
                return True

        return False