# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ans = []

        def dfs(node):
            if(not node):
                return
            if(node.left):
                dfs(node.left)
            ans.append(node.val)
            if(node.right):
                dfs(node.right)
            return
        dfs(root)

        return ans



        