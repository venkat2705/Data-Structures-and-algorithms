class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        window_char = {}
        ans = -2**32
        left,right = 0,0
        while right < n:
            if s[right] not in window_char:
                window_char[s[right]] = 1
            else:
                window_char[s[right]] += 1
            while len(window_char)>2:
                window_char[s[left]]-=1
                if window_char[s[left]] == 0:
                    del(window_char[s[left]])
                left+=1
            ans = max(ans,right - left + 1)
            right += 1
        return ans
        
            
        