# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        if(root is None):
            return True
        if((root.left is None and root.left is not None) or (root.left is not None and root.left is None)):
            return False
        


        def bfs(left, right):
            if(left is None and right is None):
                return True
            if(left is None or right is None):
                return False
            if(left.val != right.val):
                return False
            return bfs(left.left, right.right) and bfs(left.right, right.left)

        return bfs(root.left, root.right)