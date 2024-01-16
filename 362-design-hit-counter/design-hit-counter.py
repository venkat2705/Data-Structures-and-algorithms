class HitCounter:

    def __init__(self):
        self.data = []

    def hit(self, timestamp: int) -> None:
        self.data.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        ans = 0
        for i in self.data:
            if i > timestamp - 300:
                ans+=1
        return ans

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)