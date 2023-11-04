class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        ans,res = 0,0
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        s_ptr = 0
        e_ptr = 0
        while s_ptr < len(start) and e_ptr < len(end):
            if start[s_ptr]<end[e_ptr]:
                s_ptr += 1
                ans += 1
            else:
                e_ptr += 1
                ans -= 1
            res = max(ans,res)
        return res

        


        