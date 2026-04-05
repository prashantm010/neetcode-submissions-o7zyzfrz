class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        for i in range(m):
            res = self.searchInRow(matrix[i], target)
            if res:
                return True

        return False

    def searchInRow(self, arr, target):
        l, r = 0, len(arr)
        while l < r:
            m = (l + r) // 2
            if arr[m] == target:
                return True
            elif arr[m] > target:
                r = m
            else:
                l = m + 1
        return False
