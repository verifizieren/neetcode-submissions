class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) -1

        topmax = 0
        while l<r:
            curmax = min(heights[l], heights[r]) * (r - l)

            if heights[l] <= heights[r]:
                l+=1
            else:
                r-=1

            topmax = max(topmax, curmax)
    
        return topmax