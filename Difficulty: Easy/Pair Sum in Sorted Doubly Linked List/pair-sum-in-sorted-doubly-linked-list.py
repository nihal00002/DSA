# Structure of Doubly Linked List Node
'''
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def givenSumPairs(self, head, target):
        # code here
        result = []
        low = head
        high = head
        while high.next != None:
            high = high.next 
        while high != None and low.data < high.data and low != None:
            if high.data + low.data == target:
                result.append([low.data, high.data])
                low = low.next
                high = high.prev
            if high.data + low.data > target:
                high = high.prev
            if high.data + low.data < target:
                low = low.next
        return result