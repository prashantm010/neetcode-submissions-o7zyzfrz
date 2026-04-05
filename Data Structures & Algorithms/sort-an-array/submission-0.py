class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def mergeSort(nums):
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])

            return merge(left, right)

        def merge(a1, a2):
            arr = []
            i = 0
            j = 0
            while (i < len(a1) and j < len(a2)):
                if (a1[i] <= a2[j]):
                    arr.append(a1[i])
                    i+=1
                else:
                    arr.append(a2[j])
                    j+=1
                
            arr.extend(a1[i:])
            arr.extend(a2[j:])

            return arr

        return mergeSort(nums)
        