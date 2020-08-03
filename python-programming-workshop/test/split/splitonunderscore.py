
#Split a string on underscore and grab the 5th item in the list:

mystring = "Time_to_fire_up_Kowalski's_Nuclear_reactor."

nthitem= mystring.split("_")[4]
print(nthitem)
#"Kowalski's"
