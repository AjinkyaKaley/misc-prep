import string

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

class Solution:
    def __init__(self):
        self.encodeMapping = dict(zip(range(1,27), string.ascii_lowercase))
        self.encodeMapping[0] = ""

    def createTree(self,data, parentStr, arr):
        if data > 26 :
            return None
        dataToStr = parentStr + self.encodeMapping[int(data)]
        root = Node(dataToStr)
        print("New Node created : " + str(root.data))
        if len(arr) != 0:
            data = arr[0]
            newArray = arr[1:]
            root.left = self.createTree(data, dataToStr, newArray)
            if len(arr) > 1:
                data = arr[0] * 10 + arr[1]
                newArray = arr[2:]
                print("data : " + str(data) + " new Array : " + str(newArray) )
                root.right = self.createTree(data, dataToStr, newArray)
        return root

    def printLeaf(self, root):
        if root == None:
            return
        
        if root.left is None and root.right is None:
            print(root.data)
        
        self.printLeaf(root.left)
        self.printLeaf(root.right)

sln = Solution()
root = sln.createTree(0,"", [1,2,5,2,6,1])
sln.printLeaf(root)