# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if(not head):
            return
        if(not head.next):
            return
        curr = head
        i = 1
        while(curr.next):
            curr = curr.next
            i = i + 1

        node_remove = i - n + 1

        #now to remove node_remove from the linked list

        i = 1
        curr = head
        prev = None
        while(i < node_remove):
            prev = curr
            curr = curr.next
            i = i + 1

        if(not curr.next):
            prev.next = None
        if(i == 1):
            head = curr.next
            curr = None
        else:
            prev.next = curr.next
            curr = None
        return head

##approach
#find number of nodes in linked list (num_nodes)
#remove the num_nodes-n+1 node