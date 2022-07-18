
import threading

interval = 5
def boom():
    print('BOOM!')

timer = threading.Timer(interval, boom)

if __name__ == '__main__':
    timer.start()
    import time
    time.sleep(3)
    #timer.cancel()
