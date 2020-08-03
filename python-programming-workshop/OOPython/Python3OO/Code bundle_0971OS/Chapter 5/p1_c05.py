#!/usr/bin/env python3

# Chapter 5 -- Callables and Contexts
# --------------------------------------

# ..  sectnum::
#
# ..  contents::
#

# Callable
# ======================

# Callable Example #1. Inefficient.  But. It does work.
# ::

import collections.abc
class Power1( collections.abc.Callable ):
    def __call__( self, x, n ):
        p= 1
        for i in range(n):
            p *= x
        return p

pow1= Power1()
print( pow1(2, 1024) )

# Example 2. Subtle error, readily detectable.
# ::

class Power2( collections.abc.Callable ):
    def __call_( self, x, n ):
        p= 1
        for i in range(n):
            p *= x
        return p

try:
    pow2= Power2()
except TypeError as e:
    print( e)

# Example 3. Subtle error, not readily detectable.
# ::

class Power3:
    def __call_( self, x, n ):
        p= 1
        for i in range(n):
            p *= x
        return p

pow3= Power3()
try:
    print( pow3(2,1024) )
except TypeError as e:
    print( e )

# Example 4. Super Efficient.
# ::

import collections.abc
class Power4( collections.abc.Callable ):
    def __call__( self, x, n ):
        if n == 0: return 1
        elif n % 2 == 1:
            return self.__call__(x, n-1) * x
        else: # n % 2 == 0:
            t= self.__call__(x, n//2)
            return t*t

pow4= Power4()
print( pow4(2, 1024) )

# Timeit results.
# ::

import timeit
iterative= timeit.timeit( "pow1(2,1024)","""
import collections.abc
class Power1( collections.abc.Callable ):
    def __call__( self, x, n ):
        p= 1
        for i in range(n):
            p *= x
        return p

pow1= Power1()
""", number=100000 ) # otherwise it takes 2 minutes
print( "Iterative", iterative )

import timeit
recursive= timeit.timeit( "pow4(2,1024)","""
import collections.abc
class Power4( collections.abc.Callable ):
    def __call__( self, x, n ):
        if n == 0: return 1
        elif n % 2 == 1:
            return self.__call__(x, n-1) * x
        else: # n % 2 == 0:
            t= self.__call__(x, n//2)
            return t*t

pow4= Power4()
""", number=100000 )
print( "Recursive", recursive )


# Example 4, iterative, also super efficient.
# ::

import collections.abc
class Power4i( collections.abc.Callable ):
    def __call__( self, x, n ):
        p= 1
        while n != 0:
            if n % 2 == 1:
                p *= x
                n -= 1
            else: # n % 2 == 0:
                t= self.__call__(x, n//2)
                p *= t
                p *= t
                n = 0
        return p

pow4i= Power4i()
print( pow4i(2, 1024) )

# Example 5, memoization
# ::

import collections.abc
class Power5( collections.abc.Callable ):
    def __init__( self ):
        self.memo = {}
    def __call__( self, x, n ):
        if (x,n) not in self.memo:
            if n == 0:
                self.memo[x,n]= 1
            elif n % 2 == 1:
                self.memo[x,n]= self.__call__(x, n-1) * x
            elif n % 2 == 0:
                t= self.__call__(x, n//2)
                self.memo[x,n]= t*t
            else:
                raise Exception("Logic Error")
        return self.memo[x,n]

pow5= Power5()
print( pow5(2, 1024) )

import timeit
memoized= timeit.timeit( "pow5(2,1024)","""
import collections.abc
class Power5( collections.abc.Callable ):
    def __init__( self ):
        self.memo = {}
    def __call__( self, x, n ):
        if (x,n) not in self.memo:
            if n == 0:
                self.memo[x,n]= 1
            elif n % 2 == 1:
                self.memo[x,n]= self.__call__(x, n-1) * x
            elif n % 2 == 0:
                t= self.__call__(x, n//2)
                self.memo[x,n]= t*t
            else:
                raise Exception("Logic Error")
        return self.memo[x,n]

pow5= Power5()
""", number=100000 )
print( "Memoized", memoized )

# Example 6, functools memoization
# ::

from functools import lru_cache
@lru_cache(None)
def pow6( x, n ):
    if n == 0: return 1
    elif n % 2 == 1:
        return pow6(x, n-1) * x
    else: # n % 2 == 0:
        t= pow6(x, n//2)
        return t*t

print( pow6(2, 1024) )

# Some additional Callable Examples.
# The BetingStrategy superclass.
# ::

class BettingStrategy:
    def __init__( self ):
       self.win= 0
       self.loss= 0
    def __call__( self ):
        return 1

bet= BettingStrategy()
bet()
bet.win += 1
bet()
bet.loss += 1
bet()

# A stateful betting strategy. Property-based
# ::

class BettingMartingale( BettingStrategy ):
    def __init__( self ):
        self._win= 0
        self._loss= 0
        self.stage= 1
    @property
    def win(self): return self._win
    @win.setter
    def win(self, value):
        self._win = value
        self.stage= 1
    @property
    def loss(self): return self._loss
    @loss.setter
    def loss(self, value):
        self._loss = value
        self.stage *= 2
    def __call__( self ):
       return self.stage

bet= BettingMartingale()
bet()
bet.win += 1
bet()
bet.loss += 1
bet()

# Another stateful betting strategy, using ``__setattr__()`` instead
# if properties.
# ::

class BettingMartingale2( BettingStrategy ):
    def __init__( self ):
        self.win= 0
        self.loss= 0
        self.stage= 1
    def __setattr__( self, name, value ):
        if name == 'win':
            self.stage= 1
        elif name == 'loss':
            self.stage *= 2
        super().__setattr__( name, value )
    def __call__( self ):
       return self.stage

bet= BettingMartingale2()
bet()
bet.win += 1
bet()
bet.loss += 1
bet()


# Context
# =================

# With statement example 1
# ::

def slow():
    import os
    path = os.path.expanduser( "~/Documents/Work/ItMayBeAHack/itmaybeahack.com.bkup-Feb-2012.gz" )

    import re
    format_1_pat= re.compile(
        r"([\d\.]+)\s+" # digits and .'s: host
        r"(\S+)\s+"     # non-space: logname
        r"(\S+)\s+"     # non-space: user
        r"\[(.+?)\]\s+" # Everything in []: time
        r'"(.+?)"\s+'   # Everything in "": request
        r"(\d+)\s+"     # digits: status
        r"(\S+)\s+"     # non-space: bytes
        r'"(.*?)"\s+'   # Everything in "": referrer
        r'"(.*?)"\s*'   # Everything in "": user agent
    )
    import gzip
    import csv
    with open( "subset.csv", "w" ) as target:
        wtr= csv.writer( target )
        with gzip.open( path, "r" ) as source:
            line_iter= (b.decode() for b in source)
            match_iter = (format_1_pat.match( line ) for line in line_iter)
            wtr.writerows( (m.groups() for m in match_iter if m is not None) )

# Don't actualy run it, it's slow.
#

# slow()

# Another with statement example using decimal contexts
# ::

import decimal
PENNY=decimal.Decimal("0.00")
price= decimal.Decimal('15.99')
rate= decimal.Decimal('0.0075')
print( "Tax=", (price*rate).quantize(PENNY), "Fully=", price*rate )
with decimal.localcontext() as ctx:
    ctx.rounding= decimal.ROUND_DOWN
    tax= (price*rate).quantize(PENNY)
    print( "Tax=", tax )

# A simple context manager which changes a global value.
# ::

import logging, sys
class Debugging:
    def __init__( self, aName=None ):
        self.logname= aName
    def __enter__( self ):
        self.default = logging.getLogger(self.logname).getEffectiveLevel()
        logging.getLogger().setLevel( logging.DEBUG )
    def __exit__( self, exc_type, exc_value, traceback ):
        logging.getLogger(self.logname).setLevel(self.default)
        # return True # will silence an exception!

logging.basicConfig( stream=sys.stderr, level=logging.INFO )
logging.info( "Before" )
logging.debug( "Silenced before" )
with Debugging():
    logging.info( "During" )
    logging.debug( "Enabled during" )
logging.info( "Between" )
logging.debug( "Silenced between" )
with Debugging():
    logging.info( "Again" )
    logging.debug( "Enabled Again" )
logging.info( "Done" )
logging.debug( "Silenced at the end" )

# Another simple context manager which sets a global value.
# ::

import random

class KnownSequence:
    def __init__( self, seed=0 ):
        self.seed= 0
    def __enter__( self ):
        self.was= random.getstate()
        random.seed( self.seed, version=1 )
        return self
    def __exit__( self, exc_type, exc_value, traceback ):
        random.setstate( self.was )

print( tuple(random.randint(-1,36) for i in range(5)) )
with KnownSequence():
    print( tuple(random.randint(-1,36) for i in range(5)) )
print( tuple(random.randint(-1,36) for i in range(5)) )
with KnownSequence():
    print( tuple(random.randint(-1,36) for i in range(5)) )
print( tuple(random.randint(-1,36) for i in range(5)) )

# Some classes for the examples
# ::

from collections import namedtuple
card = namedtuple( 'card', 'rank,suit' )

Suits = '♣', '♦', '♥', '♠'

class Deck( list ):
    def __init__( self, size=1 ):
        super().__init__()
        for d in range(size):
            cards = [ card(r,s) for r in range(13) for s in Suits ]
            super().extend( cards )
        random.shuffle( self )

# A Context Manager as Factory example
# ::

class Deterministic_Deck:
    def __init__( self, *args, **kw ):
        self.args= args
        self.kw= kw
    def __enter__( self ):
        self.was= random.getstate()
        random.seed( 0, version=1 )
        return Deck( *self.args, **self.kw )
    def __exit__( self, exc_type, exc_value, traceback ):
        random.setstate( self.was )

for i in range(3):
    d1= Deck()
    print( d1.pop(), d1.pop(), d1.pop() )
for i in range(3):
    with Deterministic_Deck( 1 ) as d2:
        print( d2.pop(), d2.pop(), d2.pop() )

# A Context Manager as Mixin Exampl
# ::

class Deck2( list, KnownSequence ):
    def __init__( self, size=1 ):
        super().__init__()
        for d in range(size):
            cards = [ card(r,s) for r in range(13) for s in Suits ]
            super().extend( cards )
        self.raw= True
        KnownSequence.__init__(self)
    def pop( self, *args, **kw ):
        if self.raw:
            random.shuffle( self )
            self.raw= False
        return super().pop( *args, **kw )

for i in range(3):
    d1= Deck2()
    print( d1.pop(), d1.pop(), d1.pop() )
for i in range(3):
    with Deck2( 1 ) as d2:
        print( d2.pop(), d2.pop(), d2.pop() )

# A Context Manager for File Operations
# ::

import os
class Updating:
    def __init__( self, filename ):
        self.filename= filename
    def __enter__( self ):
        try:
            self.previous= self.filename+" copy"
            os.rename( self.filename, self.previous )
        except FileNotFoundError:
            # Never existed, no previous copy
            self.previous= None
    def __exit__( self, exc_type, exc_value, traceback ):
        if exc_type is not None:
            try:
                os.rename( self.filename, self.filename+ " error" )
            except FileNotFoundError:
                pass # Never even got created?
            if self.previous:
                os.rename( self.previous, self.filename )

if __name__ == "__main__":
	try:
		os.remove( "some_file" )
	except IOError as e:
		pass
	with open("some_file","w") as original:
		original.write( "Original data\n" )
	try:
		with Updating( "some_file" ):
			with open( "some_file", "w" ) as target:
				target.write( "Attempted Update\n" )
				raise Exception( "oops" )
		# ``some_file error`` left for us to examine.
		# ``some_fie`` left intact 
	except Exception:
		pass
	with open("some_file") as original:
		print( "original", original.read() )
	with open("some_file error") as problem:
		print( "error", problem.read() )
