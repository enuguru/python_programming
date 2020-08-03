
input_file = open("hello.txt", "r")
print("The hello.txt file, line-by-line using a for-loop:")
for x in input_file:
    print(x)
input_file.close()
print("All done!")
