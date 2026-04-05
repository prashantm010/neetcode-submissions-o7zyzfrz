class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mp = dict()
        for c in t:
            mp[c] = 1 + mp.get(c, 0)

        i, j = 0, 0
        min_windowSize = float("inf")
        start_index = 0
        req_c = len(t)
        n = len(s)
        while j < n:
            ch = s[j]
            if mp.get(ch, 0) > 0:
                req_c -= 1
            mp[ch] = mp.get(ch, 0) - 1

            while req_c == 0:
                # shrink the window
                current_windowSize = j - i + 1
                if current_windowSize < min_windowSize:
                    min_windowSize = current_windowSize
                    start_index = i

                mp[s[i]] += 1
                if (mp[s[i]]) > 0:
                    req_c += 1
                i += 1
            j += 1

        return (
            ""
            if min_windowSize == float("inf")
            else s[start_index : start_index + min_windowSize]
        )
