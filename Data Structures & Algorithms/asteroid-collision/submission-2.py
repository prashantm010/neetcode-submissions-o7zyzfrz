class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for ast in asteroids:
            destroyed = False
            while st and st[-1] > 0 and ast < 0:
                if st[-1] < -ast:
                    st.pop()
                    continue
                elif st[-1] == -ast:
                    st.pop()
                    destroyed = True
                    break
                else:
                    destroyed = True
                    break
            if not destroyed:
                st.append(ast)
        return st
