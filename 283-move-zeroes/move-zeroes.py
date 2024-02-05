class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [0,1,0,3,12]
        [1,0,0,3,12]
        [1,3,0,0,12]
        i = 0,1,2,3
        cur = 0,1
        """
        cur = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i],nums[cur] = nums[cur], nums[i]
                cur+=1
        
    
                   
        