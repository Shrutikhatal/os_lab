import threading
import time
import random

max_size=10
buffer=[]
mutex =threading.Lock()

class Producer(threading.Thread):
    def run(self):
        global buffer, mutex
        while True:
            item=random.randint(1,1000)
            mutex.acquire()
            if len(buffer)<max_size:
                buffer.append(item)
                print(f"produced {item}. Buffer{buffer}")
                mutex.release()
                time.sleep(random.random())

class consumer(threading.Thread):
    def run(self):
        global buffer, mutex
        while True:
            mutex.acquire()
            if len(buffer)>0:
                item=buffer.pop(0)
                print(f"consumed {item}.Buffer: {buffer}")
            mutex.release()
            time.sleep(random.random())

if __name__ == '__main__':
    Producer=Producer()
    consumer=consumer()
    Producer.start()
    consumer.start()
    Producer.join()
    consumer.join()
    