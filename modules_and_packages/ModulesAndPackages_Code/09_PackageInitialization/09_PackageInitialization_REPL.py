import pkg

print(pkg.alist)

print(pkg.mod1)

from pkg import mod1

mod1.load_data()
print(mod1)

from pkg import mod2
pkg.mod2.load_data()
x = pkg.mod2.Location()
print(x)
