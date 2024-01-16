class FileSystem:

    def __init__(self):
        self.map_path = {"" : -1}

    def createPath(self, path: str, value: int) -> bool:
        parent1 = path.split("/")[:-1]
        parent = "/".join(parent1)
        parent1 = path[:path.rfind("/")]
        # print(parent1)
        # print(parent)
        if path not in self.map_path and parent in self.map_path:
            self.map_path[path] = value
            return True
        return False

    def get(self, path: str) -> int:
        return self.map_path[path] if path in self.map_path else -1
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)