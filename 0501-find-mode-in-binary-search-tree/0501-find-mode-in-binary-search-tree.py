# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findMode(self, root):

        result = []

        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(root)

        modes = []
        max_count = 0
        current_count = 0
        prev = None

        for num in result:

            if num == prev:
                current_count += 1
            else:
                current_count = 1
                prev = num

            if current_count > max_count:
                max_count = current_count
                modes = [num]

            elif current_count == max_count:
                modes.append(num)

        return modes

        
        
        