class Solution:
    def isValid(self, s: str) -> bool:
        d = {')':'(',']':'[','}':'{'}
        st = []
        for i in s:
            if i in '({[':
                st.append(i)
            else:
                if len(st) == 0 or st.pop() != d[i]:
                    return False
                # st.pop()
        
        return True if len(st) == 0 else False
 