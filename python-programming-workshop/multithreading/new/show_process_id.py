
from multiprocessing import Process
import os

def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())

def newprocess(name):
    info('function newprocess')
    print('hello how are you doing', name)

if __name__ == '__main__':
    info('main line')
    p = Process(target=newprocess, args=('bob',))
    p.start()
    p.join()
