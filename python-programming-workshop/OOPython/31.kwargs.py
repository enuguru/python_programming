
def print_values(**kwargs):
    for key, value in kwargs.items():
        print("The value of {} is {}".format(key, value))
    print(kwargs)

print_values(my_name="Karthik", your_name="Jatin")
