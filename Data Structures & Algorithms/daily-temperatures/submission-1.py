class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        n = len(temperatures)
        res = [0 for _ in range(n)]
        for i in range(n):
            while len(st) > 0 and temperatures[st[-1]] < temperatures[i]:
                val = st.pop()
                res[val] = i - val
            st.append(i)
        return res
