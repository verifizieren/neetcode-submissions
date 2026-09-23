class Solution:
    def trap(self, height: List[int]) -> int:
        # l, r pointer, l marks the highest bar found during traversal
        # r pointer goes through incremntal by 1
        # resArea to track final area, temArea to track the last results
        # resArea only icreases, once we have found another or higher bar -> once updates

        l, r = 0, len(height) - 1
        left_max = right_max = 0
        res = 0

        while l < r:
            if height[l] <= height[r]:
                left_max = max(left_max, height[l])
                res += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                res += right_max - height[r]
                r -= 1

        return res