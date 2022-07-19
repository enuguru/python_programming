
import threading

lockvar = threading.RLock()
print(lockvar)
lockvar.acquire()
print(lockvar)
lockvar.acquire() #--> deadlock!
print(lockvar)
lockvar.acquire() #--> deadlock!
print(lockvar)
lockvar.release()
print(lockvar)
lockvar.release()
print(lockvar)
lockvar.release()
print(lockvar)

