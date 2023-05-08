import threading
import time
import random


NUM_PHILOSOPHERS = 5
FORKS = [threading.Semaphore(1) for i in range(NUM_PHILOSOPHERS)]


class PhilosopherThread(threading.Thread):
    def __init__(self, index):
        threading.Thread.__init__(self)
        self.index = index
       
    def run(self):
        left_fork = FORKS[self.index]
        right_fork = FORKS[(self.index + 1) % NUM_PHILOSOPHERS]
       
        while True:
            left_fork.acquire()
            locked = right_fork.acquire(False)
            if locked:
                break
            left_fork.release()
            time.sleep(random.random())
       
        else:
            return
       
        self.dining()
        left_fork.release()
        right_fork.release()
       
    def dining(self):
        print(f"Philosopher {self.index} starts dining.")
        time.sleep(random.random())
        print(f"Philosopher {self.index} finishes dining.")
       
if __name__ == '__main__':
    philosophers = [PhilosopherThread(i) for i in range(NUM_PHILOSOPHERS)]
    random.seed(123)
    for philosopher in philosophers:
        philosopher.start()
    for philosopher in philosophers:
        philosopher.join()



