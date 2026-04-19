from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        data = self.store.get(key, [])
        l, r = 0, len(data) - 1

        res = ""
        while l <= r:
            m = (l + r) // 2
            if data[m][0] <= timestamp:
                res = data[m][1]
                l = m + 1
            else:
                r = m - 1
        return res
        

        
