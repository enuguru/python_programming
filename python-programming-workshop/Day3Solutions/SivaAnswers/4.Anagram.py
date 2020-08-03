
# it works, good Siva
# there is a simpler better method
# can you guess?
# to think of it, i feel this method is also very simple !!!

def is_anagram(string1,string2):
    string1 = string1.replace(" ","").lower()
    string2 = string2.replace(" ","").lower()

    if len({i for i in string1 if i not in string2}) == 0:
        if len({i for i in string2 if i not in string1}) == 0:
            print("Yes,Two Strings %s & %s are an anagram"%(string1,string2))
        else:
            print("No,Two Strings %s & %s are NOT an anagram"%(string1,string2))
    else:
        print("No,Two Strings %s & %s are NOT an anagram"%(string1,string2))
    return

is_anagram("Buckethead","Death Cube K")
is_anagram("test","rest")
is_anagram("Debit card","Bad credit")
is_anagram("Motherinlaw","Woman Hitler")
