'''
155. Min Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
 

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''

#Solution1
class MinStack:

    def __init__(self):
        self.q = []
        
    def push(self, x):
        if self.q:  #也可以 len(self.q) <> 0
            self.q.append((x, min(x, self.getMin())))
        else:
            self.q.append((x,x))

    def pop(self):
        if self.q:
            self.q.pop()

    def top(self):
        if self.q:
            return self.q[-1][0]

    def getMin(self):
        if self.q:
            return self.q[-1][1]
    

#Solution2
class MinStack:

    def __init__(self):
        self.q = []
        self.min = []
        
    def push(self, x):
        if self.min:
            if x < self.min[-1]:
                self.min.append(x)
        else:
            self.min.append(x)
            
        self.q.append(x)

    def pop(self):
        temp = self.q.pop()
        if temp == self.min[-1]:
            self.min.pop()

    def top(self):
        if self.q:
            return self.q[-1]

    def getMin(self):
        if self.min:
            return self.min[-1]
