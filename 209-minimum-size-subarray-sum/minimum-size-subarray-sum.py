class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, ans = 0, 0, 2**32
        running_sum = 0
        while r < len(nums):
            running_sum += nums[r]
            while running_sum >= target:
                running_sum -= nums[l]
                ans = min(ans, r-l+1)
                l += 1
            r+=1
        return ans if ans != 2**32 else 0

            

























        # left=0
        # right=0
        # n=len(nums)
        # ans=2**32
        # run_sum=0
        # while right < n:
        #     run_sum += nums[right]
        #     while run_sum >= target:
        #         ans = min(ans, right - left + 1)
        #         run_sum -= nums[left]
        #         left+=1
        #     right += 1
        # return ans if ans!=2**32 else 0 

        

    
        