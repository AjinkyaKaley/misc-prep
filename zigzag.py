class Solution:
    def zigzag(self, s, numOfRow):
        if numOfRow == 1:
            return s
        # layout = [[0 for j in range(0,len(s)-1)] for i in range(0,numOfRows)]
        res = ["" for x in range(len(s))]
        row = 0
        dir = False
        temp = False
        for char in s:
            res[row] += char
            print(str(res))
            if row == numOfRow-1:
                temp = dir
                dir = False
                print('dir changed from ' + str(temp) +' to '+str(dir))
            elif row == 0:
                dir = True
                print('dir changed from ' + str(temp) +' to '+str(dir))

            if dir:
                row +=1
                print('row incremented : ' + str(row))
            else:
                row -=1
                print('row decremented : ' + str(row))

            
        return ''.join(res)

sln = Solution()
r = sln.zigzag('PAYPALISHIRING', 3)
print(r)