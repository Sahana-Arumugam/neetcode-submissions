# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# #two pointer method
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         curr, prev = head, None

#         while curr:
#             nxt=curr.next
#             curr.next=prev
#             prev=curr
#             curr=nxt
#         return prev


#recursion
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        newhead=head

        if not head:
            return None
        
        if head.next:
            newhead = self.reverseList(head.next)
            head.next.next = head
        head.next=None
        return newhead
        

