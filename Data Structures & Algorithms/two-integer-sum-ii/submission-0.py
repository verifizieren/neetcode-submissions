class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, val in enumerate(numbers):
            needed = target - val
            if needed in numbers:
                if needed != val:
                    if needed > val:
                        return [i + 1, numbers.index(needed) + 1]
                    return [numbers.index(needed) + 1, i + 1]