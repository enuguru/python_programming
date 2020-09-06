
#input
# 1
# 1
# 1
# 2

x = int(input())
y = int(input())
z = int(input())
n = int(input())

print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n])
