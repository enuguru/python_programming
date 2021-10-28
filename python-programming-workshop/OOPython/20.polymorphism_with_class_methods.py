
class India():
     def capital(self):
       print("New Delhi")

     def language(self):
       print("Hindi,Telugu,Marathi,Kannada,Tamizh and English")

class USA():
     def capital(self):
       print("Washington, D.C.")

     def language(self):
       print("English")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
    country.capital()
    country.language()
