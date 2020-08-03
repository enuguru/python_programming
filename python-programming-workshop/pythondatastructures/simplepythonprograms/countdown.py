

def count_down(n):
    print(n)
    if n > 0:
        return count_down(n-1)
count_down(5)
