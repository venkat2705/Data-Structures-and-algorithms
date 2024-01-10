class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        ans = 0
        for n in nums:
            if n-1 not in hashset:
                length = 1
                while n+length in hashset:
                    length += 1
                ans = max(ans,length)
        return ans

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # hash_set = set(nums)
        # ans=0
        # for n in nums:
        #     if n-1 not in hash_set:
        #         l = 0
        #         while n+l in hash_set:
        #             l+=1
        #         ans = max(l,ans)
        # return ans