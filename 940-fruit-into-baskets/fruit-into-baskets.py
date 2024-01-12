class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        d = {}
        l,r,ans = 0,0,0
        while r < len(fruits):
            if fruits[r] not in d:
                d[fruits[r]] = 1
            else:
                d[fruits[r]] += 1
            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del(d[fruits[l]])
                l+=1
            ans = max(ans,r-l+1)
            r+=1
        return ans
