class Solution:
    def jump(self, nums: List[int]) -> int:
        cur,far,ans = 0,0,0
        for i in range(len(nums)-1):
            far = max(far,i+nums[i])
            if i==cur:
                cur = far
                ans+=1
        return ans
        