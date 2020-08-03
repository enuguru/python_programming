
# a generator that yields items instead of returning a list
def firstn(n):
   num = 0
   while num < n:
     yield num
   num += 1
 
  sum_of_first_n = sum(firstn(1000000))

