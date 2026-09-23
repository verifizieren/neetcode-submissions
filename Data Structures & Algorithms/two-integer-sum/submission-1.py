class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, val in enumerate(nums):
            needed = target - val
            if needed in seen:
                return [seen[needed], i]
            
            seen[val] = i
