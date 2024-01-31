class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n=len(temperatures)
        st = []
        ans = [0]*n
        for ind,temp in enumerate(temperatures):
            while st and temp > st[-1][0]:
                st_temp,st_ind = st.pop()
                ans[st_ind] = ind - st_ind
            st.append([temp,ind])
        return ans