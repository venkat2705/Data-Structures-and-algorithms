class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sort_arr = sorted(set(arr))

        d={}
        for i in range(len(sort_arr)):
            if sort_arr[i] not in d:
                d[sort_arr[i]]=i
        for i in range(len(arr)):
            arr[i]=d[arr[i]]+1
        return arr
        