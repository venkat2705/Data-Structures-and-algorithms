class Codec:

    def __init__(self) :
        self.encode_map = {}
        self.decode_map = {}
        self.base = "http://tinyurl.com/"


    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        shortUrl = self.base + str(len(self.encode_map)+1)
        self.encode_map[longUrl] = shortUrl
        self.decode_map[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_map[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))