class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, h, ans = 0, len(nums) - 1, 0
        while l <= h:
            m = (l+h)//2
            if nums[m] >= nums[0]:
                l = m+1
            else:
                ans = m
                h = m-1
        return nums[ans]
 