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
        result = []
        # code here
        left = head 
        right = head
        while right.next != None:
            right = right.next 
        while left.data < right.data and left != None and right.prev != None:
            if left.data + right.data == target:
                result.append([left.data,right.data])
                left = left.next
                right = right.prev
            if left.data + right.data >target:
                right = right.prev
            if left.data + right.data< target:
                left = left.next
        return result