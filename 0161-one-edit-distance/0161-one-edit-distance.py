class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        ps,pt,ls,lt = 0,0,len(s),len(t)
        if abs(ls-lt)>1 or s==t:
            return False
        cnt=0
        while ps<ls and pt<lt:
            if s[ps] != t[pt]:
                cnt +=1
                if ls>lt:
                    ps+=1
                elif ls<lt:
                    pt+=1
                else:
                    ps+=1
                    pt+=1
            else:
                ps+=1
                pt+=1
        return cnt<=1
        #     if cnt>1:
        #         return False
        # return True
                    

        

            

