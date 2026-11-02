class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        negnums = [-x for x in nums]

        heapq.heapify(nums)

        while len(nums) > k:
            heapq.heappop(nums)
        
        return nums[0]