# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head 
        slow = head
        while fast is not None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                slow = head
                while slow != fast:
                    fast = fast.next
                    slow = slow.next
                return slow
        return None
            