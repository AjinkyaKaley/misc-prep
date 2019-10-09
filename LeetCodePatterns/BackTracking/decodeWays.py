import string
class Solution:
    def __init__(self):
        self.encodeMapping = dict(zip(range(1,27), string.ascii_lowercase))

    def numDecodingsDP(self,s):
        if not s:
            return 0

        dp = [0 for x in range(len(s) + 1)]

        # base case initialization
        dp[0] = 1
        dp[1] = 0 if s[0] == "0" else 1  # (1)

        for i in range(2, len(s) + 1):
            # One step jump
            if 0 < int(s[i-1:i]) <= 9:  # (2)
                dp[i] += dp[i - 1]
            # Two step jump
            if 10 <= int(s[i-2:i]) <= 26:  # (3)
                dp[i] += dp[i - 2]
        return dp[len(s)]

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        head = ""
        tail = ""
        if len(s) == 1 or len(s) == 2 :
            if len(s) == 2 and int(s) > 26:
                head = s[0:1]
                tail = s[1:]
            else:
                return self.encodeMapping[int(s)]
        else:
            head = s[0:2]
            tail = s[2:]

        print(head + "," + tail)
        if int(head) <= 26:
            _s = ""

            # self.encodeMapping[int(head[0:1])] + self.numDecodings(int(head[1:0])+ tail)
            if head[1:] != '':
                comb1 = self.numDecodings(head[1:] + tail)
                comb1.split(",")
                print("comb1: " + str(comb1))
                for c in range(0, len(comb1)):
                    if c == len(comb1) - 1:
                        _s = self.encodeMapping[int(head[0:1])] + comb1[c]
                    else:
                        _s = self.encodeMapping[int(head[0:1])] + comb1[c] + ","
            # comb1 + head[0:1]
            comb2 = self.numDecodings(tail)
            comb2.split(",")
            print("comb2: " + str(comb2))

            _sx = ""
            for cx in range(0, len(comb2)):
                if cx == len(comb2) - 1:
                    _sx = self.encodeMapping[int(head)] + comb2[cx]
                else:
                    _sx = self.encodeMapping[int(head)] + comb2[cx] + ","
            # comb2 + head
            return _s + _sx
            # return self.encodeMapping[int(head)] + self.numDecodings(tail)
        else:
            comb = self.numDecodings(head[1:]+tail)
            comb.split(",")
            print("comb: " + str(comb))

            _sxt = ""
            for cxt in range(0, len(comb)):
                if cxt == len(comb) - 1:
                    _sxt = self.encodeMapping[int(head[0])] + comb[cxt]
                else:
                    _sxt = self.encodeMapping[int(head[0])] + comb[cxt] + ","
            return _sxt
            # return self.encodeMapping[int(head[0])] + self.numDecodings(head[1:]+tail)
    

sln = Solution()
# print(sln.encodeMapping)

print(sln.numDecodingsDP('226'))
