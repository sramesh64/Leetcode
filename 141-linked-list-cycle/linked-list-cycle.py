# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if (head is None): return False
        visited = set()
        while head not in visited:
            if (head.next == None): return False
            visited.add(head)
            head = head.next
        
        return True

        