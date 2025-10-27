"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if(not root):
            return None
        queue = deque()

        queue.append(root)

        while(queue):
            size = len(queue)
            for i in range(size):
                
                a = queue.popleft()
                if(i < size - 1):
                    a.next = queue[0]
                else:
                    a.next = None
                if(a.left):
                    queue.append(a.left)
                if(a.right):
                    queue.append(a.right)

        
        return root