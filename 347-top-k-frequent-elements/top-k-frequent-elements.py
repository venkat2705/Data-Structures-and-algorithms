class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        d1 = sorted(d.items(), key = lambda x : x[1])
        print(d1)
        ans = []
        for i in d1:
            ans.append(i[0])
        return ans[len(ans)-k:]











        # d = Counter(nums)
        # mn = []
        # for key, val in d.items():
        #     heappush(mn,(val,key))
        #     if len(mn) > k:
        #         heappop(mn)
        # return [i[1] for i  in mn] 
 