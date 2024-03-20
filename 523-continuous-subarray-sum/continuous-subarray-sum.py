class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:-1}
        running_sum = 0
        for i in range(len(nums)):
            running_sum += nums[i]
            running_sum = running_sum%k
            if running_sum in d:
                if i - d[running_sum] >= 2:
                    return True
            else:
                d[running_sum] = i
        return False