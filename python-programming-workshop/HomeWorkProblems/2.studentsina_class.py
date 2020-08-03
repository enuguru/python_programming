
## python program to print the student names in a class (Menu driven program) ##

# In a class there are many students. The class
# teacher wants to use the computer store the names
# create a menu like the one given below to store,
# delete and manange all the names by the teacher
# (clue: use a list) - done

# 1. press 1 for adding new names
# 2. press 2 for deleting names
# 3. press 3 for listing all the names
# 4. press 4 for finding if the is name already existing in list
# 5. press 5 to modify the name
# 6. press 6 to exit

menu_item = 0
namelist = []
while menu_item != 6:
    flag = 0
    print("----------------------------------------------------------------")
    print("1. Press 1 for adding new names. ")
    print("2. Press 2 for deleting names. ")
    print("3. Press 3 for listing all names. ")
    print("4. Press 4 to find if the name already exists. ")
    print("5. Press 5 to modify the name if already existing. ")
    print("6. Press 6 to quit")
    print("----------------------------------------------------------------")
    
    menu_item = int(input(" Give your choice : "))
    if menu_item == 1:
        name = input(" Type in a name to add : ")
        namelist.append(name)
    elif menu_item == 2:
        del_name = input("What name would you like to remove : ")
        if del_name in namelist:
            # namelist.remove(del_name) would work just as fine
            item_number = namelist.index(del_name)
            del namelist[item_number]
            # The code above only removes the first occurrence of
            # the name.  The code below from Gerald removes all.
            # while del_name in namelist:
            #       item_number = namelist.index(del_name)
            #       del namelist[item_number]
        else:
            print(del_name," was not found. ")
    elif menu_item == 3:
        current = 1
        if len(namelist) > 0:
            while current <= len(namelist):
                print(current,".",namelist[current-1])
                current = current + 1
        else:
            print(" List is empty. ")
    elif menu_item == 4:
        old_name = input(" Give a name you would like to find: ")
        for name in namelist:
            if(old_name == name):
                print(" The name ", name, " already exists. ")
                flag = 1
        if flag == 0:
            print(old_name, " is not found. ")
    elif menu_item == 5:
        old_name = input("What name would you like to change: ")
        if old_name in namelist:
            item_number = namelist.index(old_name)
            new_name = input(" Enter the new name : ")
            namelist[item_number] = new_name
        else:
            print(old_name, " was not found. ")

print("Goodbye")
