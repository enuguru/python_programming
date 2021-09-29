import time, os
from threading import Thread, current_thread
from multiprocessing import Process, current_process


COUNT = 20000000
SLEEP = 10

def io_bound(sec):

	pid = os.getpid()
	threadName = current_thread().name
	processName = current_process().name

	print(f"{pid} * {processName} * {threadName} \
		---> Start sleeping...")
	time.sleep(sec)
	print(f"{pid} * {processName} * {threadName} \
		---> Finished sleeping...")

def cpu_bound(n):

	pid = os.getpid()
	threadName = current_thread().name
	processName = current_process().name

	print(f"{pid} * {processName} * {threadName} \
		---> Start counting...")

	while n>0:
		n -= 1

	print(f"{pid} * {processName} * {threadName} \
		---> Finished counting...")

if __name__=="__main__":
	start = time.time()

	# YOUR CODE SNIPPET HERE
	cpu_bound(COUNT)
	cpu_bound(COUNT)
	end = time.time()
	print('Time taken in seconds -', end - start)
