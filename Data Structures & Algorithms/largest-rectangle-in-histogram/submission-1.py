class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        st = []
        area = 0
        for i in range(len(heights)):
            while len(st) > 0 and heights[st[-1]] > heights[i]:
                height = heights[st.pop()]
                width = i if len(st) == 0 else i - st[-1] - 1
                area = max(area, width*height)
            st.append(i)
        return area
        