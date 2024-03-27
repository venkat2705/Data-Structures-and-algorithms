class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = Counter(text)
        if 'o' in d:
            d['o']//=2
        if 'l' in d:
            d['l']//=2
        ans = 2**31
        for i in 'balon':
            ans = min(ans, d[i])
        return ans
        