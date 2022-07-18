
import threading

lockvar = threading.Lock()
print(lockvar)
lockvar.acquire()
lockvar.release()
print(lockvar)
lockvar.acquire() #--> deadlock!
lockvar.release()
print(lockvar)


