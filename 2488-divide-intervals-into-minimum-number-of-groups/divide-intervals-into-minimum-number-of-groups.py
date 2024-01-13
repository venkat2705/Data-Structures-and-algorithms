class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        min_heap = []
        intervals.sort()
        for i in intervals:
            first, last = i[0], i[1]
            if min_heap and first > min_heap[0] :
                heapq.heappop(min_heap)
            heapq.heappush(min_heap,last)
        return len(min_heap)
