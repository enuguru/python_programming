
# this program is fine, nice logic, no comments

word = "findingno.ofuniquecharsinastring"

char_count = {i:0 for i in word}
for i in word:
    char_count[i] += 1

print(char_count)
