class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        d={}
        res = []
        for i in range(len(s)-9):
            s1 = ""
            for j in range(i,i+10):
                s1+=s[j]
            if s1 in d:
                d[s1]+=1
            else:
                d[s1] = 1
        for value in d.keys():
            if d[value] > 1:
                res.append(value)
        return res
        