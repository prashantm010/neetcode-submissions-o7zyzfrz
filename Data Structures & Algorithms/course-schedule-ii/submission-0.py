class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        mp = {x : [] for x in range(numCourses)}
        for c, p in prerequisites:
            mp[c].append(p)

        visit, cycle = set(), set()
        output = []

        def dfs(node):
            if node in cycle:
                return False
            if node in visit:
                return True
            cycle.add(node)
            for p in mp[node]:
                if not dfs(p):
                    return False
            cycle.remove(node)
            visit.add(node)
            output.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output
        