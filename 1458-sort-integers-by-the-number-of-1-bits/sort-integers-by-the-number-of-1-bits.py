class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d = {}
        res = []
        for i in arr:
            count = bin(i).count('1')
            if count not in d:
                d[count] = [i]
            else:
                d[count].append(i)
        # print(d)
        for i in sorted(d.keys()):
            d[i].sort()
            res.extend(d[i])
        return res
        # return [i[0] for i  in d]
        

        