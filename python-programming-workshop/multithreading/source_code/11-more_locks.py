
import threading

lock = threading.Lock()
print(lock)
lock.acquire()
print(lock)
lock.release()
lock.acquire() #--> deadlock!
lock.release()

#rlock = threading.RLock()
#rlock.acquire()
#rlock.acquire() # no deadlock!
#rlock.release()
#print(rlock)
#print(threading.current_thread())
