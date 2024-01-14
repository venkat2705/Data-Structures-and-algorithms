class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        l, h = 0, len(nums)-1
        while l <= h:
            m = (l+h)//2
            if nums[m] == target:
                return m
            if nums[m] >= nums[l]:
                if target >= nums[l] and target < nums[m]:
                    h = m-1
                else:
                    l = m+1
            else:
                if target > nums[m] and nums[h] >= target:
                    l = m+1
                else:
                    h = m-1
        return ans
        # ans = -1
        # low=0
        # high=len(nums) - 1
        # while low<=high:
        #     mid = (low+high)//2
        #     if nums[mid] == target:
        #         return mid
        #     if nums[mid]>=nums[low]:
        #         if nums[low]<=target and nums[mid]>target:
        #             high = mid-1
        #         else:
        #             low = mid+1
        #     else:
        #         if nums[mid]<target and nums[high]>=target:
        #             low = mid+1
        #         else:
        #             high = mid-1
        # return ans