class Solution:
    def myPow(self, x: float, n: int) -> float:
        val = x
        if (n > 0):
            val = x ** n
        else:
            val = 1.0 /(x ** abs(n))
        return val
        