
class Cube(object):
    def __init__(self, args):
        self._args = args
    def __call__(self, x, y):
        res = self._args(x,y)
        return res*res*res
@Cube
def mul_nums(x, y):
    return x * y

print(mul_nums)
print(mul_nums(4,3))
