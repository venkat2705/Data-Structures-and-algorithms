class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        right=0
        n=len(nums)
        ans=2**32
        run_sum=0
        while right < n:
            run_sum += nums[right]
            while run_sum >= target:
                ans = min(ans, right - left + 1)
                run_sum -= nums[left]
                left+=1
            right += 1
        return ans if ans!=2**32 else 0 
    
        