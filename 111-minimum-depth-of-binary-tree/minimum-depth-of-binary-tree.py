# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if (not root):
            return 0
        depth = 0
        min_depth = 1000000000000000000000000000000

        def dfs(node):
            nonlocal depth, min_depth
            if(not node):
                return

            depth += 1
            if(not(node.left or node.right)):
                min_depth = min(min_depth, depth)
            dfs(node.left)
            dfs(node.right)
            depth -= 1

        cur = root
        dfs(cur)
        return min_depth
        