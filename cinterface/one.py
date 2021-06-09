from basic_function_helper import do_square_using_c
...
my_list = np.arange(1000)
squared_list = do_square_using_c(*my_list)

def do_square_using_c(list_in):
    """Call C function to calculate squares"""
    n = len(list_in)
    c_arr_in = (c_double * n)(*list_in)
    c_arr_out = (c_double * n)()

    python_c_square(c_int(n), c_arr_in, c_arr_out)
    return c_arr_out[:]