class AuthenticationManager:

    def __init__(self, timeToLive: int):
        self.map = {}
        self.time = timeToLive

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.map[tokenId] = currentTime

    def renew(self, tokenId: str, currentTime: int) -> None:
        limit = currentTime - self.time
        if tokenId in self.map and self.map[tokenId] > limit:
            self.map[tokenId]  = currentTime

    def countUnexpiredTokens(self, currentTime: int) -> int:
        limit = currentTime - self.time
        cnt = 0
        for key in self.map:
            if self.map[key] > limit:
                cnt += 1
        return cnt


# Your AuthenticationManager object will be instantiated and called as such:
# obj = AuthenticationManager(timeToLive)
# obj.generate(tokenId,currentTime)
# obj.renew(tokenId,currentTime)
# param_3 = obj.countUnexpiredTokens(currentTime)