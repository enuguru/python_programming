
import random
import threading
import time

def can_vote(age):
    if age < 18:
        return False
    return True

def age_check(name, age):
    while not can_vote(age):
        print(f'{name} (age {age}) is getting older')
        time.sleep(1)
        age += 1
    not_old_enough.wait()
    print(f'{name} can vote!')
    return
    

if __name__ == '__main__':
    not_old_enough = threading.Barrier(3)
    t1 = threading.Thread(target=age_check, args=('ari', 15))
    t2 = threading.Thread(target=age_check, args=('derrick', 12))
    t3 = threading.Thread(target=age_check, args=('charles', 45))
    t1.start()
    t2.start()
    t3.start()
