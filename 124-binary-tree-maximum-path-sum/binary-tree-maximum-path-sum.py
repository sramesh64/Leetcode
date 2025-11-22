# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = root.val

        #returns max path sum without split
        def dfs(node):
            nonlocal res

            if(node is None):
                return 0
            
            leftMax = max(0, dfs(node.left))
            rightMax = max(0, dfs(node.right))

            res = max(res, node.val + leftMax + rightMax)

            return max(0, node.val + max(leftMax, rightMax))

        dfs(root)
        return res