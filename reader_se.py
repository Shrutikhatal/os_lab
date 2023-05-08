import threading
import time
import random

READERS = 5
WRITERS = 3

readers_count = 0
mutex = threading.Semaphore(1)
rw_mutex = threading.Semaphore(1)
read_try = threading.Semaphore(1)

class ReaderThread(threading.Thread):
    def run(self):
        global readers_count
        while True:
            read_try.acquire()
            mutex.acquire()
            readers_count += 1
            if readers_count == 1:
                rw_mutex.acquire()
            mutex.release() 
            read_try.release()

            # Reading
            print(f"Reader {self.ident} is reading.")
            time.sleep(random.random() * 3)

            mutex.acquire()
            readers_count -= 1
            if readers_count == 0:
                rw_mutex.release()
            mutex.release()

class WriterThread(threading.Thread):
    def run(self):
        while True:
            rw_mutex.acquire()

            # Writing
            print(f"Writer {self.ident} is writing.")
            time.sleep(random.random() * 3)

            rw_mutex.release()

if __name__ == '__main__':
    readers = [ReaderThread() for i in range(READERS)]
    writers = [WriterThread() for i in range(WRITERS)]
    random.seed(123)
    for reader in readers:
        reader.start()
    for writer in writers:
        writer.start()
    for reader in readers:
        reader.join()
    for writer in writers:
        writer.join()
