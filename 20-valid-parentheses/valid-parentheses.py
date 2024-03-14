class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(',']':'[','}':'{'}
        st = []
        for i in range(len(s)):
            if s[i] in ['[','{','(']:
                st.append(s[i])
            else:
                if len(st)!=0 and d[s[i]] == st[-1]:
                    st.pop()
                else:
                    return False
        return len(st) == 0 


        

