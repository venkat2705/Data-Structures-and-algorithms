class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        l, r = 0, 0
        Alice, Bob = 0, 0
        d = {"A":0, "B":0}
        while r < len(colors):
            d[colors[r]] += 1
            if r-l+1 == 3:
                if d["A"] == 3:
                    Alice += 1
                if d["B"] == 3:
                    Bob += 1
                d[colors[l]] -= 1
                l += 1
            r += 1
        print(Alice,Bob)

        return Alice > Bob