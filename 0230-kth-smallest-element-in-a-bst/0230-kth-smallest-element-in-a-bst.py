# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        self.k = k
        self.answer = None

        def inorder(node):
            if node is None:
                return
            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.answer = node.val
                return
            inorder(node.right)
        inorder(root)

        return self.answer







        
        