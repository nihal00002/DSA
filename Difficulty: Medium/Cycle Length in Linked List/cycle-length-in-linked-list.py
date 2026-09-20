''' Structure of Linked List Node
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
'''
class Solution:
    def lengthOfLoop(self, head):
        #code here
        fast = head
        slow = head
        previous = None
        while fast is not None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                count = 1
                slow = slow.next
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count
        return 0