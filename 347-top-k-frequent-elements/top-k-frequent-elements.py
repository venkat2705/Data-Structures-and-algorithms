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
        n = len(nums)
        if n == k:
            return nums

        freq_map = {}
        for val in nums:
            freq_map[val] = freq_map.get(val, 0) + 1

        # created empty buckets (freq: 1, n)
        buckets = [[] for i in range(n+1)]

        # iterate through frequency map and add values to the bucket
        for key, val in freq_map.items():
            buckets[val].append(key)
        print(buckets)
        flatten = []
        for i in range(n, -1, -1):
            for val in buckets[i]:
                flatten.append(val)
        
        top_k_freq = []
        for i in range(k):
            top_k_freq.append(flatten[i])

        return top_k_freq