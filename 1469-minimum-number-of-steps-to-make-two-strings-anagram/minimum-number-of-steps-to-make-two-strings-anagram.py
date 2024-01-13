class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = 0
        d_s = Counter(s)
        d_t = Counter(t)
        for k,v in d_s.items():
            if k in d_t:
                cnt+=abs(v-d_t[k])
            else:
                cnt+=v
        for k,v in d_t.items():
            if k not in d_s:
                cnt+=v
        return cnt//2 if cnt%2==0 else (cnt+1)//2

        