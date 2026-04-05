class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = list(zip(position,speed))
        pair.sort(reverse=True)

        st = []

        for p, s in pair:
            t = (target - p) / s
            while len(st) > 0 and st[-1] >= t:
                t = st[-1]
                st.pop()
            st.append(t)
        return len(st)