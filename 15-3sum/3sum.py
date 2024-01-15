class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            elif i == 0 or nums[i-1] != nums[i]:
                self.two_sum(i,nums,ans)
        return ans

    def two_sum(self,i,nums,ans):
        l, h  = i+1, len(nums)-1
        while l < h:
            s = nums[i] + nums[l] + nums[h]
            if s > 0:
                h -= 1
            elif s < 0:
                l += 1
            else:
                ans.append([nums[i],nums[l],nums[h]])
                l += 1
                h -= 1
                while l <= h and nums[l] == nums[l-1]:
                    l += 1


