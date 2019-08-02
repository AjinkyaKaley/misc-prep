# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """ Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        # def rserialize(root, string):
        #     """ a recursive helper function for the serialize() function."""
        #     # check base case
        #     if root is None:
        #         string += 'None,'
        #     else:
        #         string += str(root.val) + ','
        #         string = rserialize(root.left, string)
        #         string = rserialize(root.right, string)
        #     return string

        # return rserialize(root, '')

        def preorder(root,data_serialize):
            if root:
                data_serialize += [str(root.val)]
                data_serialize = preorder(root.left, data_serialize)
                data_serialize = preorder(root.right, data_serialize)
            else:
                data_serialize.append('None')
                return data_serialize
                # return self.preorder_serialize
            return data_serialize

        return ','.join(preorder(root, []))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def reconstruct(data):
            if data[0] == 'None':
                data.pop(0)
                return None

            root = TreeNode(data[0])
            data.pop(0)
            root.left = reconstruct(data)
            root.right = reconstruct(data)
            return root
        _data = data.split(",")
        return reconstruct(_data)


# Your Codec object will be instantiated and called as such:
codec = Codec()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(5)
data_list = codec.serialize(root)
codec.deserialize(codec.deserialize(data_list))

