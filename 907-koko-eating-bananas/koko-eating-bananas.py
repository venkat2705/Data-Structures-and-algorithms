class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_valid(m):
            temp = 0
            for i in piles:
                temp += ceil(i/m)
            return temp<=h
        l=1
        hi=max(piles)
        ans = sum(piles)
        while l<=hi:
            mid = (l+hi)//2
            if is_valid(mid):
                ans = min(mid,ans)
                hi=mid-1
            else:
                l=mid+1
        return ans