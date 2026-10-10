# Node class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Queue class template
class myQueue:
    def __init__(self):
        # Initialize your data members
        self.front = None
        self.rear = None
        self.count = 0

    def isEmpty(self):
        # Return True if queue is empty, else False
        return self.front is None
        
    def enqueue(self, x):
        # Add element x to the rear
        new_node = Node(x)
        
        if self.rear is None:
            self.rear = self.front = new_node
        else:
        
            self.rear.next = new_node
            self.rear = new_node
        
        self.count += 1
        
    def dequeue(self):
        if self.front is None:
            return

        popped = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        self.count -= 1
        return popped
        

    def getFront(self):
        # Return front element
        # return -1 if empty
        if self.front is None:
            return -1
        else:
            return self.front.data

    def size(self):
        # Return current size
        return self.count