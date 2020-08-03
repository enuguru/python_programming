
#!/usr/bin/python

for num in range(10,15):  #to iterate between 10 to 20
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
         j=num/i          #to calculate the quotient
         print('%d equals %d * %d' % (num,i,j))
