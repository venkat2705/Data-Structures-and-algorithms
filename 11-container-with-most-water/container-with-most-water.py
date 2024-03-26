class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, ans = 0, len(height) - 1, 0
        while l <= r:
            width = r-l
            ans = max(min(height[r],height[l])*width, ans)
            if height[l] > height[r]:
                r -= 1
            else:
                l += 1
        return ans