class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i]>0:
                break
            elif i==0 or nums[i-1] != nums[i]:
                self.two_sum(i,nums,res)
        return res

    def two_sum(self,i,nums,res):
        l,h = i+1,len(nums)-1
        while l<h:
            s = nums[i]+nums[l]+nums[h]
            if s>0:
                h-=1
            elif s<0:
                l+=1
            else:
                res.append([nums[i],nums[l],nums[h]])
                l+=1
                h-=1
                while l<=h and nums[l] == nums[l-1]:
                    l+=1
