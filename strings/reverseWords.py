class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split(" ")
        leftPtr = 0
        rightPtr = len(words)-1
        
        while leftPtr < rightPtr:
            temp = words[leftPtr]
            words[leftPtr] = words[rightPtr].strip()
            words[rightPtr] = temp.strip()
            leftPtr+=1
            rightPtr-=1
            
        return ' '.join(words)

sln = Solution()
print(sln.reverseWords("a good   example"))