class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        con_count, consecutive, ans = [], 1, 0
        for i in range(1,len(s)):
            if s[i] == s[i-1]:
                consecutive += 1
            else:
                con_count.append(consecutive)
                consecutive = 1
        con_count.append(consecutive)

        for i in range(1,len(con_count)):
            ans += min(con_count[i],con_count[i-1])
        return ans
        