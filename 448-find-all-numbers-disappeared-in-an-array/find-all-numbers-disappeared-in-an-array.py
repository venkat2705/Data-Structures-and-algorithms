class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            ind = abs(nums[i])-1
            if nums[ind] > 0 :
                nums[ind] = -nums[ind]
        print(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                ans.append(i+1)
        return ans
        