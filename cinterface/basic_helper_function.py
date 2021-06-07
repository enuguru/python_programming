"""
Define the C-variables and functions from the C-files that are needed in Python
"""
from ctypes import c_double, c_int, CDLL
import sys

lib_path = './basic_function_win32.so'#theories/basic_function_%s.so' % (sys.platform)
try:
    basic_function_lib = CDLL(lib_path)
except:
    print('OS %s not recognized' % (sys.platform))

python_c_square = basic_function_lib.c_square
python_c_square.restype = None
