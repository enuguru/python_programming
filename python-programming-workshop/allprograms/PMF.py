
from scipy import stats

import scipy as sp
import numpy as np


#import matplotlib as mpl
from matplotlib import pyplot as plt

def binom_pmf(n=4, p=0.5):
    # There are n+1 possible number of "successes": 0 to n.
    x = range(n+1)
    y = stats.binom.pmf(x, n, p)
    plt.plot(x,y,"o", color="yellow")

    # Format x-axis and y-axis.
    plt.axis([-(max(x)-min(x))*0.05, max(x)*1.05, -0.01, max(y)*1.10])
    plt.xticks(x)
    plt.title("Binomial distribution PMF for tries = {0} & p ={1}".format(n,p))
    plt.xlabel("Variate")
    plt.ylabel("Probability")
    plt.draw()

binom_pmf()
