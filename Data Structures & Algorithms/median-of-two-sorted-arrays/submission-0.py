class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        comArr = []
        i = j = 0
        total = len(nums1) + len(nums2)

        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                comArr.append(nums1[i])
                i += 1
            else:
                comArr.append(nums2[j])
                j += 1

        while i < len(nums1):
            comArr.append(nums1[i])
            i += 1
        while j < len(nums2):
            comArr.append(nums2[j])
            j += 1
        
        if total % 2 == 0:
            m = total // 2
            return (comArr[m] + comArr[m-1]) / 2
        return comArr[total // 2]