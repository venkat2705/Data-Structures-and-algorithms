class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st_s, st_t = [],[]
        for i in s:
            if i!='#':
                st_s.append(i)
            elif st_s and i=='#':
                st_s.pop()
        for i in t:
            if i!='#':
                st_t.append(i)
            elif st_t and i=='#':
                st_t.pop()
        return st_s==st_t
            
         