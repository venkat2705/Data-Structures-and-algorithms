class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cnt = 1
        cur = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt <= 2:
                nums[cur] = nums[i]
                cur += 1
        return cur
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # count = 1
        # l = 1
        # for r in range(1, len(nums)):
        #     if nums[r] == nums[r - 1]:
        #         count += 1
        #     else:
        #         count = 1
        #     if count <= 2:
        #         nums[l] = nums[r]
        #         l += 1
        # return l



        