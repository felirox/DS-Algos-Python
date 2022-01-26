#USEFUL IN THREADED PROGRAMMING

#FIFO Queue
#LIFO Queue
#Priority Queue

#If maxsize = 0, then it is infinitely long

#qsize - size of queue, empty - true if empty, full - true if full, put - enque, get - deque , task_done - processing is complete, join - some joining shit

import queue as queue
cusQ = queue.Queue(maxsize=3)
print(cusQ.empty())
print(cusQ.qsize())
cusQ.put(1)
cusQ.put(2)
cusQ.put(4)
print(cusQ.empty())
print(cusQ.full())
print(cusQ.qsize())
print(cusQ.get())
