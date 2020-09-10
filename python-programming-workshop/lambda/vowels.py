
# function that filters vowels
import itertools
def yourfun(x):
    letters = ['a', 'e', 'i', 'o', 'u']
    if x in letters:
        return True
    else:
        return False
      
# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r','a','u','e','i']

# s = eeauei
# e [e,e] a [a] u [u] e [e] i [i]
      
# using filter function
filtered = list(filter(yourfun, sequence))
s=''.join(filtered)
print(s)
for key,group in itertools.groupby(s):
    if len(list(group)) > 1:
        print(key)
      
#print('The filtered letters are:')
#for s in filtered:
#    print(s) 
