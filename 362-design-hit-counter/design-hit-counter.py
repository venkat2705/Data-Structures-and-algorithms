class HitCounter:

    def __init__(self):
        self.data = []

    def hit(self, timestamp: int) -> None:
        self.data.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        return len(self.data) - bisect_right(self.data, timestamp - 300)

        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)