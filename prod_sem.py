import threading
import time
import random

buffer_size=10
buffer=[]
mutex=threading.Semaphore(1)
empty=threading.Semaphore(buffer_size)
full=threading.Semaphore(0)

class producer(threading.Thread):
    def run(self):
        for i in range(10):
            item=random.randint(1,100)
            empty.acquire()
            mutex.acquire()
            buffer.append(item)
            print(f"producer produced item {item}")
            mutex.release()
            full.release()
            time.sleep(random.random())


class consumer(threading.Thread):
    def run(self):
        for i in range (10):
            full.acquire()
            mutex.acquire()
            item=buffer.pop(0)
            print(f"consumer consume items {item}")
            mutex.release()
            empty.release()
            time.sleep(random.random())

if __name__ == '__main__':
    producers=producer()
    consumers=consumer()
    random.seed(123)
    producers.start()
    consumers.start()
    producers.join()
    consumers.join()
    
