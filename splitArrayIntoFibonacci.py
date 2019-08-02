
class Solution:

    def splitArrayIntoFibo(self, S):

        length = len(S)
        if length < 3:
            return []
        for i in range(1, min(length//2+1, 11)):
            for j in range(1, min(length//2+1, 11)):
                temp = []
                if S[0] == '0' and i != 1:
                    continue
                if S[i] == '0' and j != 1:
                    continue
                temp.append(int(S[0:i]))
                temp.append(int(S[i:i+j]))
                #print(temp)
                #print(i,j)
                k = i+j
                while(k < length):
                    flag = False
                    t_sum = temp[-1]+temp[-2]
                    if t_sum > 2147483647:
                        break
                    sp = str(t_sum)
                    sp_len = len(sp)
                    if k+sp_len > length or S[k:k+sp_len] != sp:
                        break
                    else:
                        k = k+sp_len
                        temp.append(t_sum)
                    if k == length:
                        return temp
        return []
                

sln = Solution()
sln.splitArrayIntoFibo('123456579')
