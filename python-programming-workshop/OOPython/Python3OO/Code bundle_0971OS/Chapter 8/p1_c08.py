#!/usr/bin/env python3

# Chapter 8 -- Decorators and Mixins -- Cross-Cutting Aspects
# ------------------------------------------------------------

# ..  sectnum::
#
# ..  contents::
#

# Decorator Example 1
# ================================

# Use of builtin decorators
# ::

import math

class Angle( float ):
    __slots__ = ( "_degrees", )
    @staticmethod
    def from_radians( value ):
        return Angle(180*value/math.pi)
    def __new__( cls, value ):
        self = super().__new__(cls)
        self._degrees= value
        return self
    @property
    def radians( self ):
        return math.pi*self._degrees/180
    @property
    def degrees( self ):
        return self._degrees

b=Angle.from_radians(.227)
print( b.degrees )

# Decorator Example 2
# ================================

# Use of library decorators.
# Some preliminary definitions
# ::

Suits = '♣', '♦', '♥', '♠'

# functools.total_ordering
# ::

import functools

@functools.total_ordering
class Card:
    __slots__ = ( "rank", "suit" )
    def __new__( cls, rank, suit ):
        self = super().__new__(cls)
        self.rank= rank
        self.suit= suit
        return self
    def __eq__( self, other ):
        return self.rank == other.rank
    def __lt__( self, other ):
        return self.rank < other.rank
    def __str__( self ):
        return "{rank:d}{suit:s}".format(rank=self.rank, suit=self.suit)

c1= Card( 3, '♠' )
c2= Card( 3, '♥' )
print( "==", c1 == c2 )
print( "< ", c1 < c2 )
print( "<=", c1 <= c2 )
print( ">=", c1 >= c2 )

# Mixin example
# =======================

# ContextDecorator as mixin
# ::

from contextlib import ContextDecorator
import random

def card( rank, suit ):
    return rank, suit

class Deck( list ):
    def __init__( self, size=1 ):
        super().__init__()
        self.rng= random.Random()
        for d in range(size):
            cards = [ card(r,s) for r in range(13) for s in Suits ]
            super().extend( cards )
        self._init_shuffle()
    def _init_shuffle( self ):
        self.rng.shuffle( self )

class TestDeck( ContextDecorator, Deck ):
    def __init__( self, size= 1, seed= 0 ):
        super().__init__( size=size )
        self.seed= seed
    def _init_shuffle( self ):
        """Don't shuffle during __init__."""
        pass
    def __enter__( self ):
        self.rng.seed( self.seed, version=1 )
        self.rng.shuffle( self )
        return self
    def __exit__( self, exc_type, exc_value, traceback ):
        pass

for i in range(3):
    d1= Deck(5)
    print( d1.pop(), d1.pop(), d1.pop() )

for i in range(3):
    with TestDeck(5, seed=0) as d2:
        print( d2.pop(), d2.pop(), d2.pop() )

# Decorator Example 1
# ==============================

# Simple function decorator
# ::

import logging, sys
import functools

def debug( function ):
    @functools.wraps( function )
    def logged_function( *args, **kw ):
        logging.debug( "%s( %r, %r )", function.__name__, args, kw, )
        result= function( *args, **kw )
        logging.debug( "%s = %r", function.__name__, result )
        return result
    return logged_function

@debug
def ackermann( m, n ):
    if m == 0: return n+1
    elif m > 0 and n == 0: return ackermann( m-1, 1 )
    elif m > 0 and n > 0: return ackermann( m-1, ackermann( m, n-1 ) )

logging.basicConfig( stream=sys.stderr, level=logging.DEBUG )
print( ackermann(2,4) )

def debug2( function ):
    @functools.wraps( function )
    def logged_function( *args, **kw ):
        log= logging.getLogger( function.__name__ )
        log.debug( "call( %r, %r )", args, kw, )
        result= function( *args, **kw )
        log.debug( "result %r", result )
        return result
    return logged_function

@debug2
def ackermann( m, n ):
    if m == 0: return n+1
    elif m > 0 and n == 0: return ackermann( m-1, 1 )
    elif m > 0 and n > 0: return ackermann( m-1, ackermann( m, n-1 ) )
print( ackermann(2,4) )

# Decorator Example 2
# ==============================

# Parameterized decorator
# ::

def decorator(config):
    def concrete_decorator(function):
        def wrapped( *args, **kw ):
            return function( *args, ** kw )
        return wrapped
    return concrete_decorator

def debug_named(log_name):
    def concrete_decorator(function):
        @functools.wraps( function )
        def wrapped( *args, **kw ):
            log= logging.getLogger( log_name )
            log.debug( "%s( %r, %r )", function.__name__, args, kw, )
            result= function( *args, **kw )
            log.debug( "%s = %r", function.__name__, result )
            return result
        return wrapped
    return concrete_decorator

@debug_named( "recursion" )
def ackermann( m, n ):
    if m == 0: return n+1
    elif m > 0 and n == 0: return ackermann( m-1, 1 )
    elif m > 0 and n > 0: return ackermann( m-1, ackermann( m, n-1 ) )
print( ackermann(2,4) )


# Class Decorator 1
# ==============================

# Unit and Standard Unit
# ::

def standard( class_ ):
    class_.standard= class_
    return class_

def nonstandard( based_on ):
    def concrete_decorator( class_ ):
        class_.standard= based_on
        return class_
    return concrete_decorator

class Unit:
    factor= 1.0
    @classmethod
    def value( class_, value ):
        if value is None: return None
        return value/class_.factor
    @classmethod
    def convert( class_, value ):
        if value is None: return None
        return value*class_.factor

@standard
class INCH( Unit ):
    """inch"""
    name="in"

@nonstandard( INCH )
class FOOT( Unit ):
    """foot"""
    name= "ft"
    factor= 1/12

length= INCH.value(18)
print( FOOT.convert(length), INCH.convert(length) )

# Method Decorator
# =============================

def audit( method ):
    @functools.wraps(method)
    def wrapper( self, *args, **kw ):
        audit_log= logging.getLogger( 'audit' )
        before= repr(self)
        try:
            result= method( self, *args, **kw )
            after= repr(self)
        except Exception as e:
           audit_log.exception( '%s before %s\n after %s', method.__qualname__, before, after )
           raise
        audit_log.info( '%s before %s\nafter %s', method.__qualname__, before, after )
        return result
    return wrapper

class Hand:
    def __init__( self, *cards ):
        self._cards = list(cards)
    @audit
    def __iadd__( self, card ):
        self._cards.append( card )
        return self
    def __repr__( self ):
        cards= ", ".join( map(str,self._cards) )
        return "{__class__.__name__}({cards})".format(__class__=self.__class__, cards=cards)

logging.basicConfig( stream=sys.stderr, level=logging.DEBUG )

d= Deck()
h= Hand( d.pop(), d.pop() )
h += d.pop()
print(h)

# Class Decorator 2
# ==============================

#
# ::

import logging

# Wordy
# ::

class UglyClass1:
    def __init__( self ):
        self.logger= logging.getLogger(self.__class__.__qualname__)
        self.logger.info( "New thing" )
    def method( self, *args ):
        self.logger.info( "method %r", args )

# Non-DRY
# ::

class UglyClass2:
    logger= logging.getLogger("UglyClass2")
    def __init__( self ):
        self.logger.info( "New thing" )
    def method( self, *args ):
        self.logger.info( "method %r", args )

# Less Ugly, more DRY
# ::

def logged( class_ ):
    class_.logger= logging.getLogger( class_.__qualname__ )
    return class_

@logged
class SomeClass:
    def __init__( self ):
        self.logger.info( "New thing" )
    def method( self, *args ):
        self.logger.info( "method %r", args )

logging.basicConfig( stream=sys.stderr, level=logging.DEBUG )
uc1 = UglyClass1()
uc1.method(355/113)
uc2 = UglyClass2()
uc2.method(355/113)
x = SomeClass()
x.method(355/113)

# More Complex Decoration
# ==================================

#
# ::

def memento( class_ ):
    def memento( self ):
        return "{0.__class__.__qualname__}({0!r})".format(self)
    class_.memento= memento
    return class_

@memento
class SomeClass:
    def __init__( self, value ):
        self.value= value
    def __repr__( self ):
        return "{0.value}".format(self)

h= SomeClass(2.7)
print(h.memento())

class Memento:
    def memento( self ):
        return "{0.__class__.__qualname__}({0!r})".format(self)

class SomeClass2( Memento ):
    def __init__( self, value ):
        self.value= value
    def __repr__( self ):
        return "{0.value}".format(self)

h2= SomeClass2(2.7)
print(h2.memento())

