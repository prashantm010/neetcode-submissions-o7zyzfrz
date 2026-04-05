class Solution:

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [x for x in range(n+1)]

        def find(n):
            while(parent[n] != n):
                n = parent[n]

            return n

        def union(i, j):
            iRoot = find(i)
            jRoot = find(j)

            if (iRoot != jRoot):
                parent[jRoot] = iRoot

        for edge in edges:
            if(find(edge[0]) == find(edge[1])):
                return edge
            union(edge[0], edge[1])

        
        