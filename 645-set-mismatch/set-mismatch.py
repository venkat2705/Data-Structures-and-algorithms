class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        ans = []
        for k,v in d.items():
            if v == 2:
                ans.append(k)
        for i in range(len(nums)):
            if i+1 not in d:
                ans.append(i+1)
                break
        return ans
        

        