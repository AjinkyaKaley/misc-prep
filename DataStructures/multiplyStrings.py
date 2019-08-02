class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # shortStr = num1
        # longStr = num2
        # if len(num1) > len(num2):
        #     shortStr = num2
        #     longStr = num1
        # result = []
        # carry = 0
        # for i in range(len(shortStr)-1, -1, -1):
        #     for j in range(len(longStr)-1, -1, -1):
        #         num1 = int(shortStr[i])
        #         num2 = int(longStr[j])
        #         print(num1)
        #         product = num1*num2
        #         result += str(product % 10 + carry)
        #         carry = product/10

        res = [0] * (len(num1) + len(num2))
        for i in range(len(num1)-1, -1, -1):
            carry = 0
            for j in range(len(num2)-1, -1, -1):
                tmp = int(num1[i])*int(num2[j])+carry
                # take care of the order of the next two lines
                carry = (res[i+j+1] + tmp) // 10
                res[i+j+1] = (res[i+j+1] + tmp) % 10
            # or simply: carry, res[i+j+1] = divmod((res[i+j+1] + tmp), 10)
            res[i] += carry
        res = "".join(map(str, res))
        return '0' if not res.lstrip("0") else res.lstrip("0")

sln = Solution()
sln.multiply('123','456')
