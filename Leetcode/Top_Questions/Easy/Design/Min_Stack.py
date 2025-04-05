'''
https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.
'''


class MinStack:

    def __init__(self):

        self.min_num = []
        self.min_num.append(float('inf'))

        # use default built-in STACK (just a basic list)
        self.stack = []
            

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if val <= self.min_num[-1]:
            self.min_num.append(val)
    

    def pop(self) -> None:

        if self.min_num[-1] == self.stack[-1]:
            self.min_num.pop()

        if len(self.stack) > 1:
            self.stack.pop()
    
    def top(self) -> int:
        if len(self.stack) >= 1:
            return self.stack[-1]

    def getMin(self) -> int:
        if len(self.stack) >= 1:
            return self.min_num[-1]

    def print(self) -> None:
        print(f"Stack: {self.stack}")
        print(f"Min Stack: {self.min_num}")

class MyMinStack:

    minStack = MinStack()

    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)

    minStack.print()
    
    min_number = minStack.getMin() # return -3
    print(min_number)
    
    minStack.pop()
    
    most_recent = minStack.top()    # return 0
    print(most_recent)
    
    min_number = minStack.getMin() # return -2
    print(min_number)

    minStack.print()

