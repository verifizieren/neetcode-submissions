from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()   # stores indices, nums[q] decreasing
        res = []

        for r, x in enumerate(nums):
            # 1) maintain decreasing deque
            while q and nums[q[-1]] <= x:
                q.pop()
            q.append(r)

            # 2) remove out-of-window index from front
            left = r - k + 1
            if q[0] < left:
                q.popleft()

            # 3) record max when first window formed
            if r >= k - 1:
                res.append(nums[q[0]])

        return res
