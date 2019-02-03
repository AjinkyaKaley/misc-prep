import string
class Solution:
    def __init__(self):
        self.encodeMapping = dict(zip(range(1,27), string.ascii_lowercase))

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
        if int(head) < 26:
            # self.encodeMapping[int(head[0:1])] + self.numDecodings(int(head[1:0])+ tail)
            return self.encodeMapping[int(head)] + self.numDecodings(tail)
        else:
            return self.encodeMapping[int(head[0])] + self.encodeMapping[int(head[1])] + self.numDecodings(tail)
    

sln = Solution()
print(sln.encodeMapping)

print(sln.numDecodings('125261'))