#FIFO QUEUE

from collections import deque

cusQue  = deque(maxlen=3)
print(cusQue)
cusQue.append(1)
cusQue.append(2)
cusQue.append(3)
cusQue.append(4) #DELETED 1 AND IS ADDED AFTER 3
print(cusQue.popleft())
print(cusQue)
print(cusQue.clear())
print(cusQue)