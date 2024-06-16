class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        l, r = 0, 0
        ans = 0
        while r < len(s):
            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]]+=1
            while len(d) != r-l+1:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del(d[s[l]])
                l+=1

            ans = max(ans, r-l+1)
            r+=1
        return ans
            
            
        
        