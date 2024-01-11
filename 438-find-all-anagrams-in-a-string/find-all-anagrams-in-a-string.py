class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        l,r,k = 0,0,len(p)
        dict_p = Counter(p)
        dict_win = {}
        ans = []
        while r<len(s):
            if s[r] in dict_win:
                dict_win[s[r]] += 1
            else:
                dict_win[s[r]] = 1
            if r-l+1 == k:
                if dict_win == dict_p:
                    ans.append(l)
                dict_win[s[l]]-=1
                if dict_win[s[l]] == 0:
                    del(dict_win[s[l]])
                l+=1
            r+=1
        return ans

        