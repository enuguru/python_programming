
which_one = int(input("What month (1-12)? "))
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']
 
if 1 <= which_one <= 12:
    print("The month is", months[which_one - 1])
