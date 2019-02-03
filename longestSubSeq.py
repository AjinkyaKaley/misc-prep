class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        # if len(s) is 0:
        #     return 1
        pivotPtr = 0
        forwardPtr = 0
        list(s)
        lenOfLongestSubStr = 0
        currLenOfLongestSubStr = 0

        while pivotPtr < len(s)-1:
            # forwardPtr = backPtr + 1
            while pivotPtr <= forwardPtr and pivotPtr < len(s)-1 and s[pivotPtr] == s[pivotPtr+1]:
                pivotPtr+=1
                if forwardPtr < pivotPtr:
                    forwardPtr+=1

            # print("is "+ s[forwardPtr+1] + " "+ "in "+ substringTillNow+ " " +str(s[forwardPtr+1] not in substringTillNow))
            # print("current pivot = " + s[pivotPtr] + " , "+ "current forward ptr = " + s[forwardPtr])
            while forwardPtr < len(s)-1 and s[forwardPtr] != s[forwardPtr + 1] and s[forwardPtr+1] not in s[pivotPtr:forwardPtr+1]:
                forwardPtr +=1
                currLenOfLongestSubStr = len(s[pivotPtr:forwardPtr+1])
                print("substr till now = " + s[pivotPtr:forwardPtr+1])
            
            if currLenOfLongestSubStr > lenOfLongestSubStr:
                lenOfLongestSubStr = currLenOfLongestSubStr

            print("len of longstr = " + str(currLenOfLongestSubStr))
            currLenOfLongestSubStr = 0

            print("substr = " + s[pivotPtr:forwardPtr+1])
            pivotPtr +=1

            if pivotPtr >= forwardPtr:
                while forwardPtr < len(s)-1 and s[pivotPtr] == s[forwardPtr]:
                    forwardPtr += 1
                # forwardPtr += 1
            print("-------------------------")
        if lenOfLongestSubStr == 0 and len(s) is not 0:
            lenOfLongestSubStr = 1
        return lenOfLongestSubStr

sln = Solution()
print(sln.lengthOfLongestSubstring("pezfhjqkecapqsidubmecoqnsrulakerofyyrpivrkkheumyxzdzpvmhmjvpvb"))
