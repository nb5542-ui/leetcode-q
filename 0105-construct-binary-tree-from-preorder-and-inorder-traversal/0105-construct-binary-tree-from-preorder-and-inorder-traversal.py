# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])

        index = inorder.index(preorder[0])

        left_inorder = inorder[:index]
        right_inorder = inorder[index+1:]

        left_preorder = preorder[1:index+1]
        right_preorder = preorder[index+1:]

        root.left = self.buildTree(left_preorder,left_inorder)
        root.right = self.buildTree(right_preorder,right_inorder)

        return root
        

        
        