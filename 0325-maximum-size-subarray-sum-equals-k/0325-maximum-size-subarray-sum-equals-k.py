class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # r=0
        # l=0
        # sum1 = 0
        # ans = 0
        # while r<len(nums):
        #     sum1+=nums[r]
        #     if sum1 == k:
        #         ans = max(ans,r-l+1)
        #     while sum1>k:
        #         sum1 -= nums[l]
        #         l-=1
        # return ans
    
        res=0
        running_sum=0
        d={0:-1}
        for i in range(len(nums)):
            running_sum+=nums[i]
            if running_sum not in d:
                d[running_sum]=i
            if running_sum-k in d:
                res=max(res,i-d[running_sum-k])
        return res
        
        