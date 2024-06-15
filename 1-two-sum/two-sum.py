class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            d[diff] = i
        for i in range(len(nums)):
            if nums[i] in d and i!=d[nums[i]]:
                return [i, d[nums[i]]]
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # d = {}
        # for i in range(len(nums)):
        #     if target - nums[i] not in d:
        #         d[target - nums[i]] = i
        # for i in range(len(nums)):
        #     if nums[i] in d and i != d[nums[i]]:
        #         return [i,d[nums[i]]]