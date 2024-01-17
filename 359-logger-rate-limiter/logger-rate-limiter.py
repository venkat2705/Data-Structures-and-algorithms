class Logger:

    def __init__(self):
        self.map = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.map:
            self.map[message] = timestamp
            return True
        else:
            if self.map[message] <= timestamp - 10:
                self.map[message] = timestamp
                return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)