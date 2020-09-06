
#input_below

#12
#insert 0 5
#insert 1 10
#insert 0 6
#print
#remove 6
#append 9
#append 1
#sort
#print
#pop
#reverse
#print

#output

#[6, 5, 10]
#[1, 5, 9, 10]
#[9, 5, 1]


if __name__ == '__main__':
    N = int(input())
mylist=[]
for _ in range(N):
    args=input().split(" ") #even if you do not give " " in split it will use " " by default
    print(args)
    print(type(args))
    if args[0]=="insert":
        mylist.insert(int(args[1]),int(args[2]))
    elif args[0]=="remove":
        mylist.remove(int(args[1]))
    elif args[0]=="reverse":
        mylist.reverse()
    elif args[0]=="sort":
        mylist.sort()
    elif args[0]=='append':
        mylist.append(int(args[1]))
    elif args[0]=="print":
        print(mylist)
    elif args[0]=="pop":
        mylist.pop()
