class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        # res.append(intervals[0])
        for interval in intervals:
            if not res or res[-1][1]<interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        return res
            












        # intervals.sort()
        # res = []
        # for interval in intervals:
        #     start = interval[0]
        #     end = interval[1]
        #     if not res or res[-1][1] < start:
        #         res.append(interval)
        #     else:
        #         res[-1][1] = max(res[-1][1], end)
        # return res
         