# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = [root.val]

        #returns max path sum without split
        def dfs(node):
            if(node is None):
                return 0
            
            leftMax = max(0, dfs(node.left))
            rightMax = max(0, dfs(node.right))

            res[0] = max(res[0], node.val + leftMax + rightMax)

            return max(0, node.val + max(leftMax, rightMax))



        dfs(root)
        return res[0]