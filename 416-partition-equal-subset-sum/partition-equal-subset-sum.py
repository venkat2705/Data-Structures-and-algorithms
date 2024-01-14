class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        def rec(i,target,memo):
            if (i,target) in memo:
                return memo[(i,target)]
            if i == len(nums) :
                memo[(i,target)] = False
                return False
            if target == 0:
                memo[(i,target)] = True
                return True
            if target < 0:
                memo[(i,target)] = False
                return False
            take = rec(i+1, target-nums[i], memo)
            not_take = rec(i+1, target, memo)
            memo[(i,target)] = take or not_take
            return memo[(i,target)]
        if sum(nums) % 2:
            return False
        target = sum(nums)//2
        return rec(0,target,{})

        