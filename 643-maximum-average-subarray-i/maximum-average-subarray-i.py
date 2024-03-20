class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        r, l, ans, s = 0, 0, -2**31, 0
        while r < len(nums):
            s += nums[r]
            if r-l+1 == k:
                ans = max(ans,s/k)
                s-=nums[l]
                l+=1
            r+=1
        return ans
  