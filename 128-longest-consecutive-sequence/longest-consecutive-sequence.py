class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        ans = 0
        for i in nums:
            if i-1 not in hash_set:
                l = 1
                while i + l in hash_set:
                    l += 1
                ans = max(l,ans)
        return ans 
