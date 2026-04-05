class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ind = [0]*numCourses
        adj = {x: [] for x in range(numCourses)}
        for i, j in prerequisites:
            ind[j] += 1
            adj[i].append(j)

        q = deque()
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)

        f = 0
        while q:
            cn = q.pop()
            f += 1            
            for i in adj[cn]:
                ind[i] -= 1
                if ind[i] == 0:
                    q.append(i)


        return f == numCourses
