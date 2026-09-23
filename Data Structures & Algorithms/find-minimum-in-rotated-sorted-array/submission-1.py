class Solution:
    def findMin(self, nums: List[int]) -> int:
        TRList = ['F' if num > nums[-1] else 'T' for num in nums]
        
        l, r = 0, len(nums) -1

        while l < r:
            m = (l+r) //2

            if TRList[m] == 'T':
                r = m
            else:
                l = m + 1
        return nums[l]
    