#!/usr/bin/env python3

# Chapter 3 -- Attribute Access, Properties and Descriptors
# -----------------------------------------------------------

# This is imported later, so we're careful with the ``print()`` functions
# using ``__name__ == "__main__"`` tests.

# ..  sectnum::
#
# ..  contents::
#

__all__ = [ "RateTimeDistance" ]

# Immutability
# ======================

# Yes, this is out of order from the book.
# It belongs here to make the code below work out nicely.

# A simple-looking card class with comparisons.
# ::

import random

class BlackJackCard:
    """Abstract Superclass"""
    __slots__ = ( 'rank', 'suit', 'hard', 'soft' )
    def __init__( self, rank, suit, hard, soft ):
        super().__setattr__( 'rank', rank )
        super().__setattr__( 'suit', suit )
        super().__setattr__( 'hard', hard )
        super().__setattr__( 'soft', soft )
    def __str__( self ):
        return "{0.rank}{0.suit}".format( self )
    def __setattr__( self, name, value ):
        raise AttributeError( "'{__class__.__name__}' has no attribute '{name}'".format( __class__= self.__class__, name= name ) )
    def __lt__( self, other ):
        if not isinstance( other, BlackJackCard ):
            return NotImplemented
        return self.rank < other.rank
    def __le__( self, other ):
        try:
            return self.rank <= other.rank
        except AttributeError:
            return NotImplemented
    def __gt__( self, other ):
        if not isinstance( other, BlackJackCard ):
            return NotImplemented
        return self.rank > other.rank
    def __ge__( self, other ):
        if not isinstance( other, BlackJackCard ):
            return NotImplemented
        return self.rank >= other.rank
    def __eq__( self, other ):
        if not isinstance( other, BlackJackCard ):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit
    def __ne__( self, other ):
        if not isinstance( other, BlackJackCard ):
            return NotImplemented
        return self.rank != other.rank and self.suit == other.suit

class Ace21Card( BlackJackCard ):
    def __init__( self, rank, suit ):
        super().__init__( "A", suit, 1, 11 )

class Face21Card( BlackJackCard ):
    def __init__( self, rank, suit ):
        super().__init__( {11:'J', 12:'Q', 13:'K'}[rank], suit, 10, 10 )

class Number21Card( BlackJackCard ):
    def __init__( self, rank, suit ):
        super().__init__( str(rank), suit, rank, rank )

def card21( rank, suit ):
    if rank == 1: return Ace21Card( rank, suit )
    elif 2 <= rank < 11: return Number21Card( rank, suit )
    elif 11 <= rank < 14: return Face21Card( rank, suit )
    else:
        raise TypeError

Suits = '♣', '♦', '♥', '♠'

class Deck(list):
    def __init__(self, decks=6, factory=card21):
        super().__init__()
        for i in range(decks):
            self.extend( factory(r+1,s) for r in range(13) for s in Suits )
        random.shuffle( self )
        burn= random.randint(1,52)
        for i in range(burn): self.pop()

class BlackJackCard2( tuple ):
    """Abstract Superclass"""
    def __new__( cls, rank, suit, hard, soft ):
        return super().__new__( cls, (rank, suit, hard, soft) )
    def __getattr__( self, name ):
        return self[{'rank':0, 'suit':1, 'hard':2 , 'soft':3}[name]]
    def __setattr__( self, name, value ):
        raise NotImplementedError

class BlackJackCard3:
    """Abstract Superclass"""
    def __init__( self, rank, suit, hard, soft ):
        super().__setattr__( 'rank', rank )
        super().__setattr__( 'suit', suit )
        super().__setattr__( 'hard', hard )
        super().__setattr__( 'soft', soft )
    def __setattr__( self, name, value ):
        if name in self.__dict__:
            raise AttributeError( "Cannot set {name}".format(name=name) )
        raise AttributeError( "'{__class__.__name__}' has no attribute '{name}'".format( __class__= self.__class__, name= name ) )
    def __getattribute__( self, name ):
        if name.startswith('_'): raise AttributeError
        return object.__getattribute__( self, name )

# Comparisons
# ================

c = BlackJackCard3( 'A', '♠', 1, 11 )

card2d= card21( 2, '♦' )
card2s= card21( 2, '♠' )
card3d= card21( 3, '♦' )

def compare( a, b ):
    print( a, b, ':', '==', a==b, '<', a<b, '<=', a<=b )

compare( card2d, card2s )
compare( card2s, card3d )
try:
    compare( card2d, 2 )
except TypeError as e:
    print( "Expected", e )

# Property Decorator
# ==============================
#
# Definition of Hand using a property for the total.
# ::

class Hand:
    def __str__( self ):
        return ", ".join( map(str, self.card) )
    def __repr__( self ):
        return "{__class__.__name__}({dealer_card!r}, {_cards_str})".format(
        __class__=self.__class__,
        _cards_str=", ".join( map(repr, self.card) ),
        **self.__dict__ )
    def split( self, deck ):
        """Updates this hand and also returns the new hand."""
        assert self._cards[0].rank == self._cards[1].rank
        c1= self._cards[-1]
        del self.card
        self.card= deck.pop()
        h_new= self.__class__( self.dealer_card, c1, deck.pop() )
        return h_new

class Hand_Lazy(Hand):
    def __init__( self, dealer_card, *cards ):
        self.dealer_card= dealer_card
        self._cards= list(cards)
    @property
    def total( self ):
        delta_soft = max(c.soft-c.hard for c in self._cards)
        hard_total = sum(c.hard for c in self._cards)
        if hard_total+delta_soft <= 21: return hard_total+delta_soft
        return hard_total
    @property
    def card( self ):
        return self._cards
    @card.setter
    def card( self, aCard ):
        self._cards.append( aCard )
    @card.deleter
    def card( self ):
        self._cards.pop(-1)

# We can now work with the total value of a hand using Hand.total
# instead of hand.total().
#
# ::

if __name__ == "__main__":
    d= Deck()
    h= Hand_Lazy( d.pop(), d.pop(), d.pop() )
    print( h.total )
    h.card = d.pop()
    print( h.total )

# What's the advantage?
# Simpler syntax. We can still have lazy vs. eager calculation of
# the total value of the hand.

class Hand_Eager(Hand):
    def __init__( self, dealer_card, *cards ):
        self.dealer_card= dealer_card
        self.total= 0
        self._delta_soft= 0
        self._hard_total= 0
        self._cards= list()
        for c in cards:
            self.card = c
    @property
    def card( self ):
        return self._cards
    @card.setter
    def card( self, aCard ):
        self._cards.append(aCard)
        self._delta_soft = max(aCard.soft-aCard.hard, self._delta_soft)
        self._hard_total += aCard.hard
        self._set_total()
    @card.deleter
    def card( self ):
        removed= self._cards.pop(-1)
        self._hard_total -= removed.hard
        # Issue: was this the only ace?
        self._delta_soft = max( c.soft-c.hard for c in self._cards )
        self._set_total()
    def _set_total( self ):
        if self._hard_total+self._delta_soft <= 21:
            self.total= self._hard_total+self._delta_soft
        else:
            self.total= self._hard_total

if __name__ == "__main__":

    d= Deck()
    h= Hand_Eager( d.pop(), d.pop(), d.pop() )
    print( h.total )
    h.cards = d.pop()
    print( h.total )

    d= Deck()
    c= d.pop()
    h= Hand_Lazy( d.pop(), c, c ) # Force splittable hand
    h2= h.split(d)

    print( h )
    print( h2 )

# Eagerly Computed Attributes
# ============================

# A class where the attributes are both dictionary keys
# and named attributes.
# ::

class RateTimeDistance( dict ):
    def __init__( self, *args, **kw ):
        super().__init__( *args, **kw )
        self._solve()
    def __getattr__( self, name ):
        return self.get(name,None)
    def __setattr__( self, name, value ):
        self[name]= value
        self._solve()
    def __dir__( self ):
        return list(self.keys())
    def _solve(self):
        if self.rate is not None and self.time is not None:
            self['distance'] = self.rate*self.time
        elif self.rate is not None and self.distance is not None:
            self['time'] = self.distance / self.rate
        elif self.time is not None and self.distance is not None:
            self['rate'] = self.distance / self.time

if __name__ == "__main__":

    rtd= RateTimeDistance( rate=6.3, time=8.25, distance=None )
    print( "Rate={rate}, Time={time}, Distance={distance}".format( **rtd ) )

# Descriptors
# =====================

# A Non-Data descriptor example with local data in the descriptor.
# ::

class UnitValue_1:
    """Non-data Descriptor; data local to the descriptor."""
    def __init__( self, unit ):
        self.value= None
        self.unit= unit
        self.default_format= "5.2f"
    def __set__( self, instance, value ):
        self.value= value
    def __str__( self ):
        return "{value:{spec}} {unit}".format( spec=self.default_format, **self.__dict__)
    def __format__( self, spec="5.2f" ):
        #print( "formatting", spec )
        if spec == "": spec= self.default_format
        return "{value:{spec}} {unit}".format( spec=spec, **self.__dict__)

class RTD_1:
    rate= UnitValue_1( "kt" )
    time= UnitValue_1( "hr" )
    distance= UnitValue_1( "nm" )
    def __init__( self, rate=None, time=None, distance=None ):
        if rate is None:
            self.time = time
            self.distance = distance
            self.rate = distance / time
        if time is None:
            self.rate = rate
            self.distance = distance
            self.time = distance / rate
        if distance is None:
            self.rate = rate
            self.time = time
            self.distance = rate * time
    def __str__( self ):
        return "rate: {0.rate} time: {0.time} distance: {0.distance}".format(self)

if __name__ == "__main__":

    m1 = RTD_1( rate=5.8, distance=12 )
    print( m1 )
    print( "Time:", m1.time.value, m1.time.unit )

# A (contrived) data descriptor example with data in the instance.
# ::

class Unit:
    conversion= 1.0
    def __get__( self, instance, owner ):
        return instance.kph * self.conversion
    def __set__( self, instance, value ):
        instance.kph= value/self.conversion

class Knots( Unit ):
    conversion= 0.5399568

class MPH( Unit ):
    conversion= 0.62137119

class KPH( Unit ):
    def __get__( self, instance, owner ):
        return instance._kph
    def __set__( self, instance, value ):
        instance._kph= value

class Measurement:
    kph= KPH()
    knots= Knots()
    mph= MPH()
    def __init__( self, kph=None, mph=None, knots=None ):
        if kph: self.kph= kph
        elif mph: self.mph= mph
        elif knots: self.knots= knots
        else:
            raise TypeError
    def __str__( self ):
        return "rate: {0.kph} kph = {0.mph} mph = {0.knots} knots".format(self)

if __name__ == "__main__":

    m2 = Measurement( knots=5.9 )
    print( m2 )
    print( "Speed:", m2.mph )
