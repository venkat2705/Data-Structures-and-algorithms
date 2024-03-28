class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        cur = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[cur] = nums[cur], nums[i]
                cur += 1
            # else:
            #     nums[i], nums[cur] = nums[cur], nums[i]
        return nums
        