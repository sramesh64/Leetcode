# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node):
            if (not node):
                return None
            if (node is p or node is q):
                return node
            right = dfs(node.right)
            left = dfs(node.left)

            if (left and right):
                return node
            if(left):
                return left
            return right

        return dfs(root)