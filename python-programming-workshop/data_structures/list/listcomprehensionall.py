

one = [x.strip() for x in ('foo\n', 'bar\n', 'baz\n')]
print(one)

two =  [int(x) for x in ('1', '2', '3')]
print(two)

#using a dictionary with list comprehension
d = {'foo': '10', 'bar': '20', 'baz': '30'}
three = [d[x] for x in ['foo', 'baz']]
print(three)

d = {'foo': '10', 'bar': '20', 'baz': '30'}
four =  [int(d[x].rstrip('0')) for x in ['foo', 'baz']]
