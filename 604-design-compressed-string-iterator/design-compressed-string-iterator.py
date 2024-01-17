class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.pos = 0
        self.val = None
        self.cnt = 0
        
    def moveNext(self):
        if self.pos >= len(self.s):
            raise StopIteration
        self.val = self.s[self.pos]
        pos = self.pos + 1
        while pos < len(self.s) and self.s[pos].isdigit():
            pos += 1
        self.cnt = int(self.s[self.pos+1:pos])
        self.pos = pos

    def next(self) -> str:
        if not self.hasNext(): return ' '
        if self.cnt == 0: self.moveNext()
        self.cnt -= 1
        return self.val

    def hasNext(self) -> bool:
        return self.pos < len(self.s) or self.cnt > 0
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()