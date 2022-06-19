
import itertools

def look_and_say_pythonic(n):
	s = '1';
	for _ in range(n-1):
		s = ''.join(str(len(list(group))) + key for key, group in itertools.groupby(s))
	return s

print(look_and_say_pythonic(9))
