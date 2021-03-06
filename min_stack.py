#Minimum stack using a tuple. Returns minimum value in the stack in O(1) time

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.curr_min=self.getMin()
        if ((self.curr_min==None) or (self.curr_min > x)):
            self.curr_min=x
        self.stack.append((x,self.curr_min))

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop(-1)
        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1][0]

    def get_min(self):
        """
        :rtype: int
        """
        if len(self.stack)==0:
            return None
        else:
            return self.stack[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.get_min()
