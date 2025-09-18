# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        cur = root
        inorder = []
        stack = []

        while(cur or stack):
            while(cur):
                stack.append(cur)
                cur = cur.left
            #cur is none
            node = stack.pop()
            if(len(inorder) > 0 and node.val <= inorder[-1]):
                return False

            inorder.append(node.val)

            cur = node.right
        
        return True
        
##