
class A:
    def width(self):
        print("a, width called")

class B(A):
    def size(self):
        print("b, size called")

# Create new class instance.
b = B()
# Call method on B.
b.size()
# Call method from base class.
b.width()
