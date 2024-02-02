class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for i in operations:
            if i == 'C' and st:
                st.pop()
            elif i == 'D' and st:
                st.append(st[-1]*2)
            elif i == '+' and len(st)>=2:
                st.append(st[-1] + st[-2])
            else:
                st.append(int(i))
        return sum(st)

        