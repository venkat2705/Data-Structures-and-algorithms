class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1 = 1
        c = 1
        while p1<len(nums):
            if nums[p1] == nums[p1-1]:
                c+=1
                if c>2:
                    nums.pop(p1)
                    p1-=1
            else:
                c=1
            p1+=1
        return len(nums)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n=len(nums)
        # p1=1
        # c=1
        # while p1<len(nums) :
        #     if nums[p1]==nums[p1-1]:
        #         c+=1
        #         if c>2:
        #             nums.pop(p1)
        #             p1-=1
        #     else:
        #         c=1
        #     p1+=1
        
        

