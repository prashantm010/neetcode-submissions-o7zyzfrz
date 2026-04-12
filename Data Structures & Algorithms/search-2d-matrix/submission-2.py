class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        for i in range(n):
            res = self.searchUtils(matrix[i], target)
            if res:
                return True                

        return False
    
    def searchUtils(self, arr, t):
        l, r = 0, len(arr) - 1

        while l <= r:
            m = (l + r) // 2

            if (arr[m] == t):
                return True
            elif (arr[m] > t):
                r = m - 1
            else:
                l = m + 1
            
        return False