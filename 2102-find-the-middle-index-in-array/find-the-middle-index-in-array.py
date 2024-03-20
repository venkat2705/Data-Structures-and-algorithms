class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        ls, rs = [0]*n, [0]*n
        ls[0], rs[-1] = 0, 0
        for i in range(1,n):
            ls[i] = ls[i-1] + nums[i-1]
        for i in range(n-2,-1,-1):
            rs[i] = rs[i+1] + nums[i+1]
        for i in range(n):
            if ls[i] == rs[i]:
                return i
        return -1
        