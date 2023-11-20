class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        ans = []
        for i in nums:
            ele = a*i*i + b*i + c
            ans.append(ele)
        ans.sort()
        return ans

        
        