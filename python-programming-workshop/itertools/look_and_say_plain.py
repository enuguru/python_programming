
def lookandsay(n):
    def nextnumber(s):
        result, i = [], 0
        while i < len(s):
            count = 1
            while ((i + 1) < len(s) and s[i] == s[i + 1]):
                i = i + 1
                count = count + 1
            result.append(str(count) + s[i])
            i = i + 1
        return ''. join(result)
    s = '1'
    for _ in range(1, n):
        s = nextnumber(s)
    return s

#print(lookandsay(5))

for val in range(1,6):
    number = lookandsay(val)
    print(number)
