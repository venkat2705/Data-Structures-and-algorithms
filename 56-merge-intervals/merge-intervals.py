class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            if not res or res[-1][1] < start:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], end)
        return res
            

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # intervals.sort()
        # ans = []
        # for interval in intervals:
        #     start = interval[0]
        #     end = interval[1]
        #     if len(ans) == 0 or ans[-1][1] < start:
        #         ans.append(interval)
        #     else:
        #         ans[-1][1] = max(ans[-1][1], end)
                
        # return ans


        