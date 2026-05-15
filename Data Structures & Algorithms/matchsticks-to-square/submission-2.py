class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)

        if total % 4 != 0:
            return False

        target = total // 4

        sides = [0] * 4
        matchsticks.sort()

        def dfs(i):
            if i == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3]

            for j in range(len(sides)):
                if sides[j] + matchsticks[i] > target:
                    continue
                # Skip duplicate states
                if j > 0 and sides[j] == sides[j - 1]:
                    continue
                sides[j] += matchsticks[i]
                if dfs(i + 1):
                    return True
                sides[j] -= matchsticks[i]
            return False

        return dfs(0)
