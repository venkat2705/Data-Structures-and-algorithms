class CustomStack:

    def __init__(self, maxSize: int):
        self.st = []
        self.mx = maxSize
        self.cnt = 0

    def push(self, x: int) -> None:
        if self.cnt < self.mx :
            self.st.append(x)
            self.cnt+=1
        # print(self.st, self.cnt)

    def pop(self) -> int:
        if self.cnt <= 0:
            return -1
        self.cnt -= 1
        # print(self.st)
        return self.st.pop()
        
    def increment(self, k: int, val: int) -> None:
        i = 0
        for i in range(k):
            if i >= self.cnt:
                break
            self.st[i] += val
        
        


        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)