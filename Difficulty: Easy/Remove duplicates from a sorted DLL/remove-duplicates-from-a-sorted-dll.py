# class Node:
#     def __init__(self, value):
#         self.data = value  # value stored in node
#         self.next = None
#         self.prev = None

class Solution:
    def removeDuplicates(self, head):
        # code here
        
        current = head
        while current:
            if current.prev and current.prev.data == current.data:
                if current.prev == head:
                    current.prev = None
                    head = current   
                else:
                    current.prev.prev.next = current
                    current.prev = current.prev.prev
            current = current.next
        return head