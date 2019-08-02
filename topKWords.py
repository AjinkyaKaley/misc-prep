import heapq
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False
        self.heapRef = None
        self.count = 0

class HeapNode:
    def __init__(self, word, count=0):
        self.word = word
        self.count = count
    
    def __lt__(self, other):
        if self.count == other.count:
            return self.word < other.word
        else:
            return self.count < other.count

class Solution:
    def __init__(self):
        self.root = TrieNode()
        self.topK = []
    def addToTrie(self, word):
        crawler = self.root
        for c in word:
            if not c in crawler.children:
                crawler.children[c] = TrieNode()
            crawler = crawler.children[c]
        crawler.isEnd = True
        crawler.count -= 1

        if crawler.heapRef:
            crawler.heapRef.count -= 1
        else:
            crawler.heapRef = HeapNode(word, crawler.count)
            heapq.heappush(self.topK, crawler.heapRef)
        # self.topK.append(crawler.heapRef)
        heapq.heapify(self.topK)
    
    def findTopKWords(self, listOfWords,k):
        for word in listOfWords:
            self.addToTrie(word)
        for i in range(k):
            temp = heapq.heappop(self.topK)
            print(temp.word + " , " + str(temp.count*-1))

sln = Solution()
sln.findTopKWords(["i", "love", "leetcode", "i", "love", "coding"], 2)
