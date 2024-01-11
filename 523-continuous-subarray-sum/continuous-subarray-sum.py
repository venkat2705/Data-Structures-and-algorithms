class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:-1}
        run_sum = 0
        for i in range(len(nums)):
            run_sum += nums[i]
            run_sum = run_sum%k
            if run_sum in d:
                if i-d[run_sum]>=2:
                    return True
            else:
                d[run_sum] = i
        return False