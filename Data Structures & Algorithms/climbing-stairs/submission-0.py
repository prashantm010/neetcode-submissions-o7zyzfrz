class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [0 for x in range(n+1)]
        return self.ans(n, mem)

    def ans(self, n, mem):
        if n <= 1:
            return 1
        if (mem[n] > 0):
            return mem[n]
        o1 = self.ans(n-1, mem)
        o2 = self.ans(n-2, mem)
        mem[n] = o1 + o2
        return mem[n]
        