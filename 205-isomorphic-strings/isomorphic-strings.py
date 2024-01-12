class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}
        for x,y in zip(s,t):
            if x not in ds:
                ds[x] = y
            else:
                if ds[x]!=y:
                    return False
            if y not in dt:
                dt[y] = x
            else:
                if dt[y]!=x:
                    return False
        return True


        