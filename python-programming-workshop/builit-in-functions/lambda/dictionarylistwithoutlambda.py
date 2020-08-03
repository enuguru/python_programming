

def f1(x): return x ** 2

def f2(x): return x ** 3

def f3(x): return x ** 4

key = 'quadratic'
print({'square': f1, 'cubic': f2, 'quadratic': f3}[key](10))
