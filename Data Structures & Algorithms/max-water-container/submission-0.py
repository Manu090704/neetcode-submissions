class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0, len(heights) - 1
        maxContainer = 0
        while l < r:
            width = abs(l - r)
            minHight = min(heights[l], heights[r])
            actualContainer = width * minHight
            maxContainer = max(actualContainer, maxContainer)
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxContainer

        