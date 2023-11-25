class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d={}
        res=[]
        for i in range(len(s)-9):
            s1 = ""
            for j in range(i,i+10):
                s1 += s[j]
            if s1 in d:
                d[s1]+=1
            else:
                d[s1] = 1
        for key in d.keys():
            if d[key] > 1:
                res.append(key)
        return res
                
        