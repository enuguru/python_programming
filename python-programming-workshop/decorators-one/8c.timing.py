
import time

def timing_decorator(that_function):

#prints the time a function takes to run

    def wrapper():
        t1 = time.time()
        that_function()
        t2 = time.time()
        print("Hello")
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"

    return wrapper

@timing_decorator
def new_function():
    new_list = []
    for num in (range(0, 10000000)):
        new_list.append(num)
    print("\nSum of all the numbers: " + str((sum(new_list))))

print(new_function())
#new_function()
