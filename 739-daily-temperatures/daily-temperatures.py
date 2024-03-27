class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st, res = [], [0]*len(temperatures)
        for ind, temp in enumerate(temperatures):
            while st and temp > st[-1][0]:
                st_temp, st_ind = st.pop()
                res[st_ind] = ind - st_ind
            st.append([temp, ind])
        return res
  