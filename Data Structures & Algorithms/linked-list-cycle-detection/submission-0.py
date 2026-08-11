# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        seen = {}

        cur = head
        while cur:
            nxt = cur.next
            if not seen:
                seen[cur] = seen.get(cur,0)+1
            elif nxt in seen:
                return True
            else:
                seen[nxt] = seen.get(nxt,0)+1
            cur = nxt
        return False