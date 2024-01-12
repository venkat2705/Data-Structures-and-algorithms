class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o','u']
        l, r, ans, res = 0, 0, 0, 0
        d = {}
        while r < len(s):
            if s[r] in vowels:
                ans += 1
            res = max(ans,res)
            if r-l+1==k:
                if s[l] in vowels:
                    ans-=1
                l+=1
            r+=1
        return res
                

