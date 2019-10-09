"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children



class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: Node
        :rtype: str
        """
        if root:
            d = {'value': root.val, 'children': []}
            if root.children:
                for child in root.children:
                    d['children'] += [self.serialize(child)]
            return d
        else:
            return {}

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: Node
        """
        print(data)

root = Node(1,[])
two = Node(2,[])
three = Node(3,[])
four = Node(4,[])
five = Node(5,[])
six = Node(6,[])

root.children.append(three)
root.children.append(two)
root.children.append(four)
three.children.append(five)
three.children.append(six)


# Your Codec object will be instantiated and called as such:
codec = Codec()
_d = codec.serialize(root)
codec.deserialize(_d)
