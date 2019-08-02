class TrieNode:
    def __init__(self):

        self.children = [ None for letter in range(97,122)]
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):

        crawler = self.root

        for letter in range(len(word)):
            locateChild = ord(word[letter]) - ord('a')
            if crawler.children[locateChild] is None:
                crawler.children[locateChild] = TrieNode()
            crawler = crawler.children[locateChild]
        crawler.isEndOfWord = True
    
    def search(self, word):
        crawler = self.root

        for letter in word:
            locateChild = ord(letter) - ord('a')
            if not crawler.children[locateChild]:       ## is None
                return False
            crawler = crawler.children[locateChild]
        
        return crawler != None and crawler.isEndOfWord 

sln = Trie()
keys = ["the","a","there","anaswe","any","by","their"] 
output = ["Not present in trie","Present in tire"]

for k in keys:
    sln.insert(k)

print(sln.search("the"))
print(sln.search("there"))
print(sln.search("tire"))
