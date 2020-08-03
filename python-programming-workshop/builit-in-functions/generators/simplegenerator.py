
def simple_generator_function():
   yield 1
   yield 2
   yield 3

for value in simple_generator_function():
    print(value)

our_generator = simple_generator_function()
print(next(our_generator))
print(next(our_generator))
print(next(our_generator))
