

#Python program that uses try, else

while True:
    # Read int from console.
    denominator = int(input())

    # Use int as denominator.
    try:
        i = 1 / denominator
    except:
        print("Error")
    else:
        print("OK")
