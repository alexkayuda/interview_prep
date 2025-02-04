import queue
from collections import deque


# First In, First Out (FIFO) principle.
# The first element added is the first one to be removed.

# Create a queue
q = queue.Queue()

# Enqueue some items
q.put(1)
q.put(2)
q.put(3)

# Dequeue an item
item = q.get()
print(item)  # Output: 1

# Check if queue is empty
print(q.empty())  # Output: False