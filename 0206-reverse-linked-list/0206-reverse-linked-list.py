# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        previous = None
        current = head
        
        while current is not None:
            front = current.next
            current.next = previous
            previous = current
            current = front
        return previous