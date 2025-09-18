# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        curr_depth = 0
        best_depth = 0
        def dfs(node):
            nonlocal curr_depth, best_depth
            if(not node):
                return
            curr_depth += 1
            best_depth = max(best_depth, curr_depth)
            dfs(node.left)

            dfs(node.right)
            curr_depth -= 1
        
        dfs(root)
        return best_depth
            
#we want to increment 1 every time we go down, and decrement every time we come back up
        