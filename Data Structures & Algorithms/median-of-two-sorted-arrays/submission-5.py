class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m = len(nums1)
        n = len(nums2)
        
        l, r = 0, m

        while l <= r:
            x = (l + r) // 2
            y = (m + n + 1) // 2 - x

            a1 = nums1[x-1] if x > 0 else float("-inf")
            a2 = nums1[x] if x < m else float("inf")

            b1 = nums2[y-1] if y > 0 else float("-inf")
            b2 = nums2[y] if y < n else float("inf")

            if a1 <= b2 and b1 <= a2:
                if (m + n) % 2 == 0:
                    return (max(a1, b1) + min (a2, b2)) / 2
                else:
                    return max(a1, b1)
            elif a1 > b2:
                r = x - 1
            else:
                l = x + 1

