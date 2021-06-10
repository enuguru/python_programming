import concurrent.futures
import time

def myfunc(name):
  print(f'myfunc started with {name}')
  time.sleep(10)
  print(f'myfunc ended with {name}')

if __name__ == '__main__':
  print('main begins')
  with concurrent.futures.ThreadPoolExecutor(max_workers=3) as e:
    e.map(myfunc, ['Vikas', 'Riyaz', 'Reena'])
  print('main ended')
