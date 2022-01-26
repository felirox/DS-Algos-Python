from multiprocessing import Queue

cusQ = Queue(maxsize=3)
cusQ.put(1)
cusQ.put(2)
print(cusQ.get())