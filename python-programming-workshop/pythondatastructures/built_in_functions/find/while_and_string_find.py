
#While. Suppose we want to loop over all instances of a string within another string. 
#A while-loop with find can accomplish this. We use the result of find to advance the 
#starting index.

#Tip: We could optimize this sample further. Try changing the second argument to find to 
#add the length of string.

#And: This will avoid searching all the characters within a found substring. This avoids 
#finding overlapping strings.

#Python program that uses string find, while

value = "cat picture is cat picture"

# Start with this value.
location = -1

# Loop while true.
while True:
    # Advance location by 1.
    location = value.find("picture", location + 1)

    # Break if not found.
    if location == -1: break

    # Display result.
    print(location)
