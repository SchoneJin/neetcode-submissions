class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0

        while l < r:
            tmp = min(heights[l], heights[r]) * (r - l)

            if tmp > res:
                res = tmp
            
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

        return res