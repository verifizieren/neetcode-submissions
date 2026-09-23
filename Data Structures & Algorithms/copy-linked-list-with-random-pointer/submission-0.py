"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        nodeMap = {}
        
        cur = head
        dummy = Node(0)
        copy_cur = dummy

        while cur:
            copy = Node(cur.val)
            nodeMap[cur] = copy
            copy_cur.next = copy
            copy_cur = copy
            cur = cur.next

        cur = head
        copy_cur = dummy.next
        while cur:
            copy_cur.random = nodeMap[cur.random] if cur.random else None
            cur = cur.next
            copy_cur = copy_cur.next
        
        return dummy.next