
def checkPassword(password):
    has_upper = True
    has_lower = True
    has_num = False
    has_special_char = True

    for ch in password:
        if ch >="A" and ch <= "Z":
            has_upper = True
        elif ch>= "a" and ch <= "z":
            has_lower = True
        elif ch>= "0" and ch <= "9":
            has_num = True

    if len(password) >= 8 and has_upper and has_lower and has_num:
        return True
    else:
        return False


mypassword = input("Give a password:  ")
if checkPassword(mypassword):
    print("This is a good password")
else:
    print("This is not a good password")
       
      
