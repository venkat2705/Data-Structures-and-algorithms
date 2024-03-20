class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        r, l, zero_cnt, ans = 0, 0, 0, 0
        while r < len(nums):
            if nums[r] == 0:
                zero_cnt += 1
            while zero_cnt > k:
                if nums[l] == 0:
                    zero_cnt -= 1
                l+=1
            ans = max(ans, r-l+1)
            r+=1
        return ans















        # right = 0
        # left  = 0
        # ans = 0
        # running_zeros = 0
        # while right < len(nums):
        #     if nums[right] == 0:
        #         running_zeros += 1
        #     while running_zeros > k:
        #         if nums[left] == 0:
        #             running_zeros -= 1
        #         left+=1
        #     ans = max(ans,right-left+1)
        #     right+=1
        # return ans

        
        