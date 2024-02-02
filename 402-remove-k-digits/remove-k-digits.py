class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        st = []
        for i in num:
            while k>0 and st and st[-1] > i:
                k-=1
                st.pop()
            st.append(i)
        st = st[:len(st)-k]
        i = 0
        while( i <len(st) and st[i] == "0" ):
            i += 1
            
        return ''.join(st[i:]) if (len(st[i:]) > 0) else "0" 


        