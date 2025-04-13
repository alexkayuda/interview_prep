'''
Deque is a double-ended queue with O(1) time for append/pop operations from both sides. 
Used as stacks and queues.
'''

from collections import deque

# ---------------------------------------------------------------------------------------------

# Create a Stack (First IN - Last Out)
stack = deque()

# Push to stack
stack.append(4)
stack.append(5)
stack.append(6)

print(stack) # Output: deque([4, 5, 6])

# Pop from Stack
stack.pop() # Pop returns an element that is being removed. Capture it if neeed.
stack.pop()

print(stack) # Output: deque([4])

my_list = list(stack)
print(my_list) # Output 4

# Peek Stack
print(stack[-1]) # Output: 4

# ---------------------------------------------------------------------------------------------

# Create a Queue (First IN - Last Out)
queue = deque()

# Push to Queue
queue.appendleft(1)
queue.appendleft(2)
queue.appendleft(3)

print(queue) # Output: deque([3, 2, 1])

# Pop from Queue
queue.pop()
queue.popleft()

print(queue) # Output: deque([2])

my_list = list(queue)
print(my_list) # Output [2]

# ---------------------------------------------------------------------------------------------
# Additional Features

dq = deque('bcde') # creates a list of ['b', 'c', 'd', 'e']
dq.append('f')
dq.appendleft('a')

print(dq) # Output: deque(['a', 'b', 'c', 'd', 'e', 'f'])


dq.rotate(1) # rotate 1 step to the right
print(dq)    # Output: deque(['f', 'a', 'b', 'c', 'd', 'e'])

dq.rotate(-2) # rotate 2 steps to the left
print(dq)    # Output: deque(['b', 'c', 'd', 'e', 'f', 'a'])
