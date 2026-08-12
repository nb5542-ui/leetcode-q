# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):

        result = []

        def inorder(node):

            if node is None:
                return

            inorder(node.left)

            result.append(node.val)

            inorder(node.right)

        inorder(root)

        for i in range(1, len(result)):
            if result[i] <= result[i - 1]:
                return False

        return True
        
        

            
        

    


          
        