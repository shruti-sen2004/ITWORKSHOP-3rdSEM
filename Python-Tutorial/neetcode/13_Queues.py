from collections import deque

# deque - double ended queue
# insertion and deletion from both ends
queue = deque()
queue.append(1) # append right
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)
queue.appendleft(6) # append left

print(queue)

queue.popleft() # pop left; constant time unlike stack
queue.pop() # pop right

print(queue)