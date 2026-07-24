# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):

        def dfs(node):

            
            if not node:
                return (0, 0)

            leftRob, leftNotRob = dfs(node.left)
            rightRob, rightNotRob = dfs(node.right)
 
            rob = node.val + leftNotRob + rightNotRob
 
            notRob = max(leftRob, leftNotRob) + max(rightRob, rightNotRob)

            return (rob, notRob)

        robRoot, notRobRoot = dfs(root)
        return max(robRoot, notRobRoot)

        
        