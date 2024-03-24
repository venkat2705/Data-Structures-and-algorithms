class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l, r, ans = 0, 0, []
        d_p = Counter(p)
        d = {}
        while r < len(s):
            if s[r] in d:
                d[s[r]] += 1
            else:
                d[s[r]] = 1
            if r - l + 1 == len(p):
                if d == d_p:
                    ans.append(l)
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del(d[s[l]])
                l += 1
            r += 1
        return ans
