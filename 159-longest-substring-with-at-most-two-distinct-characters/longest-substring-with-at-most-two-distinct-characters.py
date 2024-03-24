class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l, r, ans = 0, 0, -2**31
        d = {}
        while r < len(s):
            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]] += 1
            
            while len(d) > 2:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del(d[s[l]])
                l += 1
            ans = max(ans,r-l+1)
            r += 1
        return ans
        

                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # n = len(s)
        # window_char = {}
        # ans = -2**32
        # left,right = 0,0
        # while right < n:
        #     if s[right] not in window_char:
        #         window_char[s[right]] = 1
        #     else:
        #         window_char[s[right]] += 1
        #     while len(window_char)>2:
        #         window_char[s[left]]-=1
        #         if window_char[s[left]] == 0:
        #             del(window_char[s[left]])
        #         left+=1
        #     ans = max(ans,right - left + 1)
        #     right += 1
        # return ans
        
            
        