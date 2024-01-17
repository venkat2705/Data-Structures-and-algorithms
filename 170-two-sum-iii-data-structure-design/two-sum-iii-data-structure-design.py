class TwoSum:

    def __init__(self):
        self.list = []

    def add(self, number: int) -> None:
        self.list.append(number)

    def find(self, value: int) -> bool:
        d = {}
        if len(self.list) < 2:
            return False
        for i in range(len(self.list)):
            d[value - self.list[i]] = i
        for i in range(len(self.list)):
            if self.list[i] in d and i != d[self.list[i]]:
                return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)