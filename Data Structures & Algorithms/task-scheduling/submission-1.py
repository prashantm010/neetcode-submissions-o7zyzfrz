import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        c_map = dict()
        for ele in tasks:
            c_map[ele] = c_map.get(ele, 0) + 1

        print(c_map)
        hp = [-v for v in c_map.values()]
        heapq.heapify(hp)

        counter = 0

        while len(hp) > 0:
            i = 0
            temp = []

            while i <= n:
                if hp:
                    abc = heapq.heappop(hp) + 1
                    if abc != 0:
                        temp.append(abc)

                counter += 1
                i += 1
                if not hp and not temp:
                    break

            hp.extend(temp)
            heapq.heapify(hp)
        return counter
