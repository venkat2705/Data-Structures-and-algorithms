class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # we are counting number of meetings going on in parallel and the max of that will be the total number of rooms that we need

        start, end = [], []
        for i in intervals:
            start.append(i[0])
            end.append(i[1])
        start.sort()
        end.sort()
        p1, p2, rooms_cnt, ans  = 0, 0, 0, 0
        while p1 < len(start) and p2 < len(end):
            if start[p1] < end[p2]:
                rooms_cnt += 1
                p1 += 1
            else:
                rooms_cnt -= 1
                p2 += 1
            ans = max(ans, rooms_cnt)
        return ans


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # start, end = [], []
        # for i in intervals:
        #     start.append(i[0])
        #     end.append(i[1])
        # start.sort()
        # end.sort()
        # s_ptr, e_ptr, meetings_cnt, ans = 0, 0, 0, 0
        # while s_ptr < len(start) and e_ptr < len(end):
        #     if start[s_ptr] < end[e_ptr]:
        #         meetings_cnt += 1
        #         s_ptr += 1
        #     else:
        #         meetings_cnt -= 1
        #         e_ptr += 1
        #     ans = max(ans,meetings_cnt)
        # return ans