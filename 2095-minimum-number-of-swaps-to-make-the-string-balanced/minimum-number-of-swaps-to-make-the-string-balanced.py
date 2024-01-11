class Solution:
    def minSwaps(self, s: str) -> int:
        extra_closed,ans = 0,0
        for i in s:
            if i == ']':
                extra_closed += 1
            else:
                extra_closed -= 1
            ans = max(ans,extra_closed)
        return (ans+1)//2

        