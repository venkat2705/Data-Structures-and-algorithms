class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        res = []
        for interval in intervals:
            if len(res) == 0 or res[-1][1] < interval[1] :
                if res and res[-1][0] == interval[0]:
                    res[-1][1] = max(res[-1][1], interval[1])
                else:
                    res.append(interval)
                
                # res[-1][1] = max(res[-1][1], interval[1])
        print(res)
        return len(res)


        