class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        d = {}
        for i in range(len(arr)):
            if abs(x-arr[i]) in d:
                d[abs(x-arr[i])].append(i)
            else:
                d[abs(x-arr[i])] = [i]
        d = dict(sorted(d.items()))
        temp = []
        for key,v in d.items():
            temp.extend(v)
        
        for i in range(len(temp)):
            temp[i] = arr[temp[i]]

        temp = temp[0:k]
        # print(temp)
        temp.sort()
        # print(temp)
        return temp


        