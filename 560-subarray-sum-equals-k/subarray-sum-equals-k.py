class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0:1}
        run_sum, ans = 0, 0
        for i in range(len(nums)):
            run_sum += nums[i]
            if run_sum - k in d:
                ans += d[run_sum - k]
            if run_sum in d:
                d[run_sum] += 1
            else:
                d[run_sum] = 1
        return ans 
 