class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        for i in range(len(nums)):
            if nums[i] in d:
                d[nums[i]][0] += 1
                d[nums[i]][2] = i
            else:
                d[nums[i]] = [1,i,i]
        print(d)
        deg,ans = 0,2**32
        for k,v in d.items():
            if v[0] >= deg:
                deg = v[0]
        for lis in d.values():
            if lis[0] == deg:
                ans = min(ans,lis[2]-lis[1]+1)
        return ans