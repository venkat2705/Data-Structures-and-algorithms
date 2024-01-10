class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur_tank, total_tank,ans = 0,0,0
        for i in range(len(gas)):
            cur_tank += gas[i]-cost[i]
            total_tank += gas[i]-cost[i]
            if cur_tank<0:
                ans = i+1
                i=i+1
                cur_tank = 0

        return ans if total_tank >=0 else -1

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # cur_tank,total_tank,start_pos = 0,0,0
        # for i in range(len(gas)):
        #     cur_tank+=gas[i]-cost[i]
        #     total_tank+=gas[i]-cost[i]
        #     if cur_tank<0:
        #         start_pos = i+1
        #         cur_tank = 0
        # return start_pos if total_tank>=0 else -1

        