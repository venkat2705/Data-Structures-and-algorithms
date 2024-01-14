class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start, end = [], []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        s_ptr, e_ptr, meetings_cnt, ans = 0, 0, 0, 0
        while s_ptr < len(start) and e_ptr < len(end):
            if start[s_ptr] < end[e_ptr]:
                meetings_cnt += 1
                s_ptr += 1
            else:
                meetings_cnt -= 1
                e_ptr += 1
            ans = max(ans,meetings_cnt)
        return ans