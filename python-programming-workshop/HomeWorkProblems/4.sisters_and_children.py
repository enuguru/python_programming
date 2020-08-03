
## python program to print the particular values using the key in dictionary ##

# There are 3 sisters in a family, all of them have
# 3 children each. Take the names of the sisters and each of
# their three children and store them. write a program to print
# the names of children, if the sister's name is given

sister_one = input(" Give the name of 1st sister : ")
sister_two = input(" Give the name of 2nd sister : ")
sister_three = input(" Give the name of 3rd sister : ")

family = {sister_one:["Ravi","Ram","Raj"],sister_two:["Thivya","Santhana"], \
sister_three:["Liya","Angel"]}

print(" Children in Family of three sisters are : ",family)

#family["HariPriya"] = ["Ranjith","Raghav"]
print("Children of fourth sister after inclusion : ",family)


print(" Children in the Family of second Sister alone are : ",family[sister_two])



