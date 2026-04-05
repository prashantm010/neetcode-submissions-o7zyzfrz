class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            mp[crs].append(pre)

        visits = set()

        def dfs(crs):
            if crs in visits:
                return False
            if mp[crs] == []:
                return True

            visits.add(crs)
            for pre in mp[crs]:
                if not dfs(pre): 
                    return False
            visits.remove(crs)
            mp[crs] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs): 
                return False

        return True

        