class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        p_s = self.get_previous_smaller_elements(heights)
        n_g = self.get_next_greater_elements(heights)

        largest = 0
        for i in range(len(heights)):
            largest = max(largest, (n_g[i] - p_s[i] - 1) * heights[i])

        return largest

    def get_previous_smaller_elements(self, heights):
        st = []
        res = [-1] * len(heights)
        for i in range(len(heights)):
            while len(st) > 0 and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                res[i] = st[-1]
            st.append(i)
        return res

    def get_next_greater_elements(self, heights):
        st = []
        res = [len(heights)] * len(heights)
        for i in range(len(heights) - 1, -1, -1):
            while len(st) > 0 and heights[st[-1]] >= heights[i]:
                st.pop()
            if st:
                res[i] = st[-1]
            st.append(i)
        return res
