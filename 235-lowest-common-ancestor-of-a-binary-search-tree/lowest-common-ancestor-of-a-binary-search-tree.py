# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        p, q = min(p.val, q.val), max(p.val, q.val)
        def dfs(node):
            if(not node):
                return
            if (p <= node.val and q >= node.val):
                return node
            if(q < node.val):
                return dfs(node.left)
            if(p > node.val):
                return dfs(node.right)

        return dfs(root)