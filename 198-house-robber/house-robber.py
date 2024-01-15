class Solution:
    def rob(self, nums: List[int]) -> int:
        def rec(i,memo):
            if i in memo:
                return memo[i]
            if i >= len(nums):
                memo[i] = 0
                return 0
            rob = nums[i] + rec(i+2,memo)
            not_rob = rec(i+1,memo)
            ans = max(rob,not_rob)
            memo[i] = ans
            return ans
        return rec(0,{})
        
















        # def rec(i,nums,memo):
        #     if i in memo:
        #         return memo[i]
        #     if i >= len(nums):
        #         memo[i] = 0
        #         return 0
        #     not_robbed = rec(i+1,nums,memo)
        #     robbed = rec(i+2,nums,memo) + nums[i]
        #     ans = max(robbed,not_robbed)
        #     memo[i] = max(robbed,not_robbed)
        #     return ans 
        # return rec(0,nums,{})