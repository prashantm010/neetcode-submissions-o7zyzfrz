from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)

        if max(freq.values()) > ((len(s) + 1) / 2):
            return ""

        heap = [(-cnt, ch) for ch, cnt in freq.items()]
        heapq.heapify(heap)

        res = []
        prev_ch = ""
        prev_cnt = 0
        while heap:
            cnt, ch = heapq.heappop(heap)
            res.append(ch)
            if prev_cnt < 0:
                heapq.heappush(heap, (prev_cnt, prev_ch))

            prev_ch, prev_cnt = ch, cnt + 1

        return "".join(res)
