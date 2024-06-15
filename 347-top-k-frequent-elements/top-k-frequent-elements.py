class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d= Counter(nums)
        heap = []
        for key, val in d.items():
            heappush(heap, (val, key))
            if len(heap) > k:
                heappop(heap)
        return [i[1] for i in heap]












        # d = {}
        # for i in nums:
        #     if i in d:
        #         d[i] += 1
        #     else:
        #         d[i] = 1
        # mn = []
        # for key, val in d.items():
        #     heappush(mn, (val,key))
        #     if len(mn)>k:
        #         heappop(mn)
        # return [i[1] for i in mn]











        # d = Counter(nums)
        # mn = []
        # for key, val in d.items():
        #     heappush(mn,(val,key))
        #     if len(mn) > k:
        #         heappop(mn)
        # return [i[1] for i  in mn] 
 