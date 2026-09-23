import heapq
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        res = []

        for i, num in enumerate(nums):
            # push negative for max heap behavior
            heapq.heappush(heap, (-num, i))

            # remove elements outside window
            while heap[0][1] <= i - k:
                heapq.heappop(heap)

            # once first window formed
            if i >= k - 1:
                res.append(-heap[0][0])

        return res
