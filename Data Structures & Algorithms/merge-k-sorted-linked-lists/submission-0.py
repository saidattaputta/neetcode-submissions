# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        values = []

        for head in lists:

            cur = head
            while cur:
                values.append(cur.val)
                cur = cur.next
        values.sort()

        dummy = ListNode(0)
        cur = dummy
        for i in values:
            cur.next = ListNode(i)
            cur = cur.next
        return dummy.next