class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        n = len(present)
        def dfs(i,budget,memo):
            if (i,budget) in memo:
                return memo[(i,budget)]
            if i==n:
                memo[(i,budget)] = 0
                return 0
            buy = 0
            if budget >= present[i]:
                buy = future[i] - present[i] + dfs(i+1,budget - present[i],memo)
            not_buy = dfs(i+1,budget,memo)
            ans = max(buy,not_buy)
            memo[(i,budget)] = ans
            return ans
        return dfs(0,budget,{})
 