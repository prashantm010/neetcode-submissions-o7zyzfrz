from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        return self.search(self.timeMap[key], timestamp)

    def search(self, pairs: list[tuple[int, str]], timestamp: int) -> str:
        l, r = 0, len(pairs) - 1
        while l < r:
            m = (l + r + 1) // 2
            if pairs[m][0] <= timestamp:
                l = m
            else:
                r = m - 1
        return pairs[l][1] if pairs[l][0] <= timestamp else ""
