
def cat(filenames):
    for f in filenames:
        for line in open(f):
            print(line)


cat('one')
