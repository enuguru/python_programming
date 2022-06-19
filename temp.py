

import functools

def ss_decode_col_id(col):
    return functools.reduce(lambda result,c: result*26 + ord(c) - ord('A'),col,0)

excelcolid = input("Give the Column id ")
print(ss_decode_col_id(excelcolid))
