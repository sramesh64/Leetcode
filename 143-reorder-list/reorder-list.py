# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        while(fast.next and fast.next.next):
                fast = fast.next.next
                slow = slow.next

        #now reverse everything after slow
        prev = None
        curr = slow.next
        slow.next = None

        while(curr):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next


        #now curr points to head of linked list b, head points to head of linked list a
        #want to merge the two linked lists, a1 b1 a2 b2
        curr = prev
        while(curr):
            nexta = head.next
            nextb = curr.next
            curr.next = head.next
            head.next = curr
            curr = nextb
            head = nexta

        

        
