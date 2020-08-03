
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('python is awesome'):
    print(char)
