class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l,r = 0,0
        zc = 0
        ans = -2**31
        while r<len(nums):
            if nums[r] == 0:
                zc += 1
            
            while zc > 1:
                if nums[l] == 0:
                    zc-=1
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans