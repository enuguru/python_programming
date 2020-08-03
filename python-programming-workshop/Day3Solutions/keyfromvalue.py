

// dictionaires are not supposed to be used this way
// that is trying to find the key corresponding to the value

def keyfromvalue(s):
    
    dictionary = {"scenic":34, "superb":39, "great":1000}
    for key,value in dictionary.items():
        if value == s:
            print(key)
            break
    else:
        print("There is no key corresponding to the value")

myvalue = int(input("Give a value"))
keyfromvalue(myvalue)
