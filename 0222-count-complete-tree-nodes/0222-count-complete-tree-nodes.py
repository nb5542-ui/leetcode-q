# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root):

        def count(node):

            if node is None:
                return 0

            left = count(node.left)
            right = count(node.right)

            return left + right + 1
        return count(root)
        