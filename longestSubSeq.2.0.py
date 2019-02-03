import string
class Solution:

    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
            
        visited = dict.fromkeys(list(s), -1)
        print(visited)
        visited[s[0]] = 0
        currLength = 1
        maxSubStrLen = 1
        for i in range(1,len(s)):

            prevIndex = visited[s[i]]
            if prevIndex == -1 or (i - currLength > prevIndex):
                currLength +=1
            else:
                if currLength > maxSubStrLen:
                    maxSubStrLen = currLength
                currLength = i - prevIndex
            visited[s[i]] = i

        if currLength > maxSubStrLen:
            maxSubStrLen = currLength
        return maxSubStrLen





sln = Solution()
print(sln.lengthOfLongestSubstring("au"))
