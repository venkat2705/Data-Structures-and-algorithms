class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        k, j = n-1, n-1
        while k>0 and nums[k-1] >= nums[k]:
            k -= 1
        if k == 0:
            nums.reverse()
            return
        while nums[k-1] >= nums[j]:
            j -= 1
        nums[j], nums[k-1] = nums[k-1], nums[j]
        nums[k:] = nums[n-1: k-1: -1]
        
  