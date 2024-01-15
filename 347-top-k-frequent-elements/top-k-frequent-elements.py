class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        instead of sorting the dictionary in a reverse order, which takes O(NlogN). We can consider other approaches as well
        1. using priority queue (comparision will be frequency of the element)--> O(Nlogk)
        2. using bucket sort 
            a. create frequency map
            b. create buckets and add each element into frequency bucket 
            c. iterate from the end of the buckets and add values to an array
            d. return array till k index
        '''
        d = Counter(nums)
        d = sorted(d.items(), key = lambda items : items[1])
        print(d)
        ans = []
        for i in d:
            ans.append(i[0])
        return ans[len(ans)-k:]