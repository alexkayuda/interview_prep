from collections import deque

queue = deque(["Eric", "John", "Michael"])

queue.append("Terry")           # Terry arrives

queue.append("Graham")          # Graham arrives

queue.popleft()                 # The first to arrive now leaves -> Removes 'Eric'

queue.popleft()                 # The second to arrive now leaves -> Removes 'John'

print(queue)                           # Remaining queue in order of arrival
#deque(['Michael', 'Terry', 'Graham'])

