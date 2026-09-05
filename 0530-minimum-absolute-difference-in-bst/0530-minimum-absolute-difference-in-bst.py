# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        result = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        min_diff = float("inf")

        for i in range(len(result) - 1):
            min_diff = min(min_diff, abs(result[i + 1] - result[i]))

        return min_diff
        
   






    




        
        