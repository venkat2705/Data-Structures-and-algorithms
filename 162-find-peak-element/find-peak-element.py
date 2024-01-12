class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        l,h = 0,n-1
        while l <= h:
            m = l + ((h-l)//2)
            
            if m<n-1 and nums[m+1]>nums[m]:
                l=m+1
            elif m>0 and nums[m-1]>nums[m]:
                h=m-1
            else:
                return m
        


        
        
        