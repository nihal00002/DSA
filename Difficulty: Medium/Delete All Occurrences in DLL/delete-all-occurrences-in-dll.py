# Structure of the doubly linked list Node 
# class Node:
#     def __init__(self, x):
#         self.data = x
#         self.next = None
#         self.prev = None

class Solution:
    def deleteAllOccurOfX(self, head, x):
        temp = head
        new_head = head
        prev = None
        while temp != None:
            next_node = temp.next  
            if temp.data == x:
                if prev != None:
                    prev.next = temp.next
                if temp.next != None:
                    temp.next.prev = prev
                if temp == new_head:
                    new_head = new_head.next
               
            else:
                prev = temp 
            temp = next_node
        return new_head