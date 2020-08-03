
    # function that filters vowels
    def yourfun(x):
        letters = ['a', 'e', 'i', 'o', 'u']
        if x in letters:
            return True
        else:
            return False
      
      
    # sequence
    sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r','a','u']
      
    # using filter function
    filtered = filter(yourfun, sequence)
      
    print('The filtered letters are:')
    for s in filtered:
        print(s) 
