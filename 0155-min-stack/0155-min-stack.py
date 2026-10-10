class MinStack(object):

    def __init__(self):
        self.stack = []
        
    def push(self, value):
        """
        :type value: int
        :rtype: None
        """
        if not self.stack:
            mini = value
        else:
            mini = min(value,self.stack[-1][1])

        self.stack.append([value,mini])

        

    def pop(self):
        """
        :rtype: None
        """
        self.stack.pop()
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()