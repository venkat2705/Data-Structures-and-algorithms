class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l,h = 0,len(nums)-1
        while l<=h:
            m = (l+h)//2
            # print(l,h,m)
            if (m+1)%2 == 1:
                # print(l,h,m)
                if m<len(nums)-1 and  nums[m+1] == nums[m]:
                    l=m+1
                
                elif m>0 and nums[m-1] == nums[m]: 
                    h=m-1
                else:
                    return nums[m]
            
            else:
                if m>0 and nums[m-1] == nums[m]:
                    l=m+1
                elif m<len(nums)-1 and nums[m+1] == nums[m]: 
                    h=m-1
                else:
                    return nums[m]
            print(l,h,m)

        