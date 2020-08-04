
names = ['lakshna','ragavendra','abinav','aprameya','kirthika','sreeram','rishi','uma','sreenivasan','narayanan','sahasrashree','haripriya','adarsh']

nameone = input("Give a name")
nametwo = input("Give one more name")

if (nameone not in names) or (nametwo not in names):
    print("your name is not in the list")
else:
    if (nameone == 'abinav' or nameone =='lakshna') and (nametwo == 'lakshna' or nametwo == 'abinav'):
        print("you are welcome")
    else:
        print("better luck next time")

