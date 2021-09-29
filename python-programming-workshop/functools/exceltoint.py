
def decode(col):
    c=ord('A')
    print(c)
    ret=0
    for i in col:
        i=ord(i)
        print(i)
        ret=(ret*26)+i-c+1
    return ret

col = input("enter a valid excel column id")
col = col.upper()
print(decode(col))

