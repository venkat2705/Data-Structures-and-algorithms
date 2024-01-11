import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heap,ans = [],[]
        for i in nums:
            heapq.heappush(heap,i)
        while heap:
            a = heapq.heappop(heap)
            ans.append(a)
        return ans