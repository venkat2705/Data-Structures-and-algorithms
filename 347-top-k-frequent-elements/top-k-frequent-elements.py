class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        mn = []
        for key, val in d.items():
            heappush(mn,(val,key))
            if len(mn) > k:
                heappop(mn)
        return [i[1] for i  in mn] 
 