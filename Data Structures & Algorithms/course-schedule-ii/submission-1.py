class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ind = [0]*numCourses
        adj = {x: [] for x in range(numCourses)}
        for i, j in prerequisites:
            ind[j] += 1
            adj[i].append(j)

        q = deque()
        for i in range(numCourses):
            if ind[i] == 0:
                q.append(i)

        output = []
        while q:
            cn = q.popleft()
            output.append(cn)      
            for i in adj[cn]:
                ind[i] -= 1
                if ind[i] == 0:
                    q.append(i)
        if len(output) != numCourses:
            return []
        return output[::-1]
        