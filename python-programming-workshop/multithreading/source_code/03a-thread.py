import time
import threading 

def myfunc(name):
    print(f'myfunc started with {name}')
    time.sleep(10)
    print('myfunc ended')

print('main started')
t = threading.Thread(target=myfunc, args=['Hi friends'])
t.start()
print('main ended')
