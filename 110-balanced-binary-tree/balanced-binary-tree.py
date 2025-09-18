# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        curr_depth, best_depth = 0, 0
        def depth(node):
            if(not node):
                return 0
            else:
                return (1 + max(depth(node.left), depth(node.right)))
                
        cur = root
        if(not(cur)): return True
        if(not (cur.left or cur.right)):
            return True
        if(not cur.left):
            return depth(cur.right) <= 1
        if(not cur.right):
            return depth(cur.left) <= 1
        if ((abs(depth(cur.left) - depth(cur.right)) > 1)): return False

        return (self.isBalanced(cur.left) and self.isBalanced(cur.right) )

        return True

        