class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def left_find(nums, target):
            l, h, ans = 0, len(nums)-1, -1
            while l <= h:
                m = (l+h)//2
                if nums[m] == target:
                    ans = m
                    h = m-1
                elif nums[m] > target:
                    h = m-1
                else:
                    l = m+1
            return ans
        
        def right_find(nums, target):
            l, h, ans = 0, len(nums)-1, -1
            while l <= h:
                m = (l+h)//2
                if nums[m] == target:
                    ans = m
                    l = m+1
                elif nums[m] > target:
                    h = m-1
                else:
                    l = m+1
            return ans
        
        left_most = left_find(nums, target)
        right_most = right_find(nums, target)
        return [left_most, right_most]
        
































        # def left(nums, target):
        #     l, h, ans = 0,len(nums) - 1, -1
        #     while l <= h:
        #         m = (l+h)//2
        #         if nums[m] == target:
        #             ans = m
        #             h = m-1
        #         elif nums[m] < target:
        #             l = m + 1
        #         else:
        #             h = m - 1
        #     return ans
        
        # def right(nums, target):
        #     l, h, ans = 0,len(nums) - 1, -1
        #     while l <= h:
        #         m = (l+h)//2
        #         if nums[m] == target:
        #             ans = m
        #             l = m + 1
        #         elif nums[m] < target:
        #             l = m + 1
        #         else:
        #             h = m - 1
        #     return ans
        # first = left(nums, target)
        # last = right(nums, target)
        # return [first, last]
