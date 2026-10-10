''' Structure of linked list Node
 class Node:
    def __init__(self, val):
        self.data = val
        self.next = None 
'''

class myStack:

    def __init__(self):
        # Initialize your data members
        self.front = None
        self.rear = None
        self.count = 0
        

    def isEmpty(self):
        # Check if the stack is empty
        return self.front is None
        

    def push(self, x):
        # Adds element x to the top of the stack
        new_node = Node(x)
            
        new_node.next = self.front
        self.front = new_node
        
        if self.rear is None:
            self.rear = new_node
            
        self.count += 1
        
        

    def pop(self):
        # Removes an element from the top of the stack
        if self.front is None:
            return -1
        popped = self.front.data 
        
        self.front = self.front.next
        
        if self.front is None:
            self.rear = None
        self.count -= 1
        return popped
        


    def peek(self):
        # Returns the top element of the stack
        # If the stack is empty, return -1
        if self.front is None:
            return -1
        return self.front.data
        


    def size(self):
        # Returns the current size of the stack
        return self.count
        
        
        
        
        
        
        