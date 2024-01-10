class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        ans = []
        for key,val in d.items():
            if val>len(nums)//3:
                ans.append(key)
        return ans


        
        
        
        
        
        
        
        
        
        
        
        
        # d=Counter(nums)
        # ans=set()
        # for i in nums:
        #     if d[i]>len(nums)//3:
        #         ans.add(i)
        # return ans
        