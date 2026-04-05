class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        mp = {x: [] for x in range(n)}
        visit = set()
        for u, v in edges:
            mp[u].append(v)
            mp[v].append(u)

        print(mp)
        def dfs(n, p):
            if n in visit:
                return False
            
            visit.add(n)
            for i in mp[n]:
                if i != p:
                    if not dfs(i, n):
                        return False
            return True

        if not dfs(0, -1):
            return False
        return len(visit) == n