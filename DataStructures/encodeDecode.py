class Solution:

    def encode(self, strs):
        return ''.join('%d:' % len(s) + s for s in strs)
    # 1:h1:e1:l1:l1:o1:w1:o1:r1:l1:d
    # '5:63/Rc1:h13:BmI3FS~J9#vmk8:7uBZ?7*/5:24h+X2:O '

    def decode(self, s):
        strs = []
        i = 0
        while i < len(s):
            j = s.find(':', i)
            i = j + 1 + int(s[i:j])
            strs.append(s[j+1:i])
        return strs

    # def encode(self, strs):
    #     result = ''
    #     for s in strs:
    #         result += (str(len(s)) + ' ' + s)

    #     return result

    # def decode(self, s):
    #     result = []
    #     i = 0
    #     while i < len(s):
    #         n = 0
    #         current = ''
    #         while s[i].isdigit():
    #             n = n*10 + int(s[i])
    #             i += 1

    #         i += 1  # skip the splitting space

    #         for j in range(n):
    #             current += s[i]
    #             i += 1

    #         result.append(current)

    #     return result

sln = Solution()
# '5:63/Rc1:h13:BmI3FS~J9#vmk8:7uBZ?7*/5:24h+X2:O '
x = sln.encode(["63/Rc", "h", "BmI3FS~J9#vmk", "7uBZ?7*/", "24h+X", "O "])
print(sln.decode(x))
