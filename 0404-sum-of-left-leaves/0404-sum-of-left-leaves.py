# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        def dfs(node):
            if node is None:
                return 0
            if (
                node.left and 
                node.left.left is None and
                node.left.right is None
            ):
                left_sum = node.left.val
            else:
                left_sum = dfs(node.left)

            right_sum = dfs(node.right)

            return left_sum + right_sum

        return dfs(root)
            

        
        