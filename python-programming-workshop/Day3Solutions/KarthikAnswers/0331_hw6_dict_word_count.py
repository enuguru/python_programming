
# no comments karthick program is well done, super

temp_str = """
A busy bee busy as ever
goes to a garden
as always and finds honey as ever
in the garden"""

temp_list = temp_str.split()
temp_dict = {}
i = 0
# print(temp_str.split())

for temp_word in iter(temp_list):
    if temp_word in temp_dict:
        i = temp_dict[temp_word]
        i += 1
        temp_dict[temp_word] = i
    else:
        temp_dict[temp_word] = 1

print (temp_dict)
