class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_set = set(nums)
        for i in range(len(nums)+1):
            if i not in hash_set:
                return i












        # nums.sort()
        # n = len(nums) 
        # for i in range(n):
        #     if i != nums[i]:
        #         return i
        # return n
        

        