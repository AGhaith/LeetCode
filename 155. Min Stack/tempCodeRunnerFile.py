class MinStack(object):
    
    stack = []
    min=int(1e9)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if(val <= min):
            self.min=val
            self.stack.append(self.min)
        self.stack.append(val)
        
        

    def pop(self):
        """
        :rtype: None
        """
        if (self.stack.pop()==self.min):
            self.min=self.stack.pop()
            
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()