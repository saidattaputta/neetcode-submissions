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
        
        cur = head
        nodelist = {}

        while cur:
            nodelist[cur] = Node(cur.val)
            cur = cur.next
        
        cur = head
        while cur:
            nodelist[cur].next = nodelist.get(cur.next)
            nodelist[cur].random = nodelist.get(cur.random)
            cur = cur.next
        return nodelist[head]