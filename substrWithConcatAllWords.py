from collections import deque
from collections import Counter
from collections import defaultdict

class Solution:

    def findSubstring(self, s: str, words):
        lookup = set(words)
        k = len(min(words, key=len))
        prevPart = ''
        idxOfPrevPart = 0
        result = []
        i=0
        while i < len(s):
            substr = s[i:i+k]
            if substr in lookup and prevPart != '' and idxOfPrevPart + len(prevPart) == i:
                result.append(s.find(prevPart + substr))
                i += k
            elif substr in lookup and prevPart == '':
                prevPart = substr
                idxOfPrevPart = i
                i += k
            elif prevPart != '':
                prevPart = ''
                i += 1
            else:
                i += 1

        print(result)
    
    def findSubstringLeetCode(self, s, words):
        n, m, r = len(words), len(words[0]) if words else 0, []
        counter = Counter(words)

        for i in range(m):
            localCout = defaultdict(int)
            window = deque()
            for j in range(i, len(s), m):
                word = s[j:j + m]
                print(word)
                if word in counter:
                    localCout[word] += 1
                    window.append(word)

                    while localCout[word] > counter[word]:
                        localCout[window.popleft()] -= 1

                    if len(window) == n:
                        r.append(j - (n - 1) * m)
                else:
                    localCout.clear()
                    window.clear()
        return r


sln = Solution()
print(sln.findSubstringLeetCode('barfoofoobarman',
                        ["foo", "bar"]))
