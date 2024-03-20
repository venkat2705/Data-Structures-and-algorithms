class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        m = len(firstList)
        n = len(secondList)
        p1, p2, ans = 0, 0, []
        while p1 < m and p2 < n:
            start = max(firstList[p1][0], secondList[p2][0])
            end = min(firstList[p1][1], secondList[p2][1])
            if start <= end:
                ans.append([start, end])
            if firstList[p1][1] < secondList[p2][1]:
                p1 += 1
            else:
                p2 += 1
        return ans
