# janus.py
from multiprocessing import Process, Lock, Queue
import random
import time

def lprint(lock, *args):
    lock.acquire()
    print(*args)
    lock.release()

def shout(lock, queue):
    for x in range(0, 10):
        message = f"{x + 1}"
        nap = random.choice([True, False, False, False])
        if nap:
            message += " then napping"

        lprint(lock, "Shouting:", message)
        queue.put(message)

        if nap:
            time.sleep(0.1)

    queue.put("done")

def hear(lock, queue):
    message = queue.get()

    while message != "done":
        lprint(lock, "Heard:", message)
        message = queue.get()

if __name__ == "__main__":
    lock = Lock()
    queue = Queue()

    p1 = Process(target=shout, args=(lock, queue))
    p2 = Process(target=hear, args=(lock, queue))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
