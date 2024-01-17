class MyHashSet:

    def __init__(self):
        self.map = {}

    def add(self, key: int) -> None:
        if key not in self.map:
            self.map[key] = 1

    def remove(self, key: int) -> None:
        if key in self.map:
            del(self.map[key])

    def contains(self, key: int) -> bool:
        return True if key in self.map else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)