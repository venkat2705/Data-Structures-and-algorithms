class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        def rec(i, color, costs,memo):
            if (i,color) in memo:
                return memo[(i,color)]
            total_cost = costs[i][color]
            if i == len(costs) - 1:
                pass
            elif color==0:
                total_cost+=min(rec(i+1,1,costs,memo),rec(i+1,2,costs,memo))
            elif color==1:
                total_cost+=min(rec(i+1,0,costs,memo),rec(i+1,2,costs,memo))
            else:
                total_cost+=min(rec(i+1,0,costs,memo),rec(i+1,1,costs,memo))
            memo[(i,color)] = total_cost
            return total_cost
        if len(costs) == 1:
            return min(costs[0])
        return min(rec(0, 0, costs,{}),rec(0, 1, costs,{}),rec(0, 2, costs,{}))
        