# A single-threaded CPU-bound program
import time
from threading import Thread

# The bottleneck of the code which is CPU-bound
def upgrade():
    number = 0
    while number < 400000000:
        number=number+1

# Recording the time taken to excecute
start = time.time()
upgrade()
end = time.time()

print('Time taken in seconds ', end - start)

#>  Time taken in seconds - 2.6532039642333984
