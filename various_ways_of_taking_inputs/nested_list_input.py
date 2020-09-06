
#5
#Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39


score_names={}
n=int(input())
for i in range(n):
    name=input().split()
    score=float(input())
    if score in score_names:
        score_names[score].append(name)
    else:
        score_names[score]=[name]

mylist=[]
for score in score_names:
    mylist.append(score)
mylist.sort()
results=score_names[mylist[1]]
results.sort()
for name in results:
    print(*name)
