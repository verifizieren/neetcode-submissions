class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        while True:
            fast = nums[fast]
            fast = nums[fast]
            slow = nums[slow]

            if fast == slow:
                break
        finder = nums[0]

        while finder != slow:
            finder = nums[finder]
            slow = nums[slow]
        
        return finder