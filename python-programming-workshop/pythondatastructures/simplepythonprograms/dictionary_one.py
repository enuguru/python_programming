
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel

tel['jack']

del tel['sape']
tel['irv'] = 4127
tel

list(tel.keys())

sorted(tel.keys())

'guido' in tel

'jack' not in tel
