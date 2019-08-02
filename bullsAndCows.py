class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        _s = zip(secret)
        _g = zip(guess)
        # print(enumerate(_s)[0])
        # for i in range(len(secret)):
        #     if enumerate(_s)[0]

sln = Solution()
sln.getHint(secret="1807", guess = "7810")
