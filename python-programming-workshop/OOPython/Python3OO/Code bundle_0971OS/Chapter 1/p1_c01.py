#!/usr/bin/env python3

# Chapter 1 -- The ``__init__()`` Method
# -----------------------------------------

# ..  sectnum::
#
# ..  contents::
#

# Simple Objects: Cards
# ==============================

# Definition of a simple class hierarchy
# ::

class Card:
    insure= False
    def  __init__( self, rank, suit ):
        self.suit= suit
        self.rank= rank
        self.hard, self.soft = self._points()
    def __eq__( self, other ):
        return self.suit == other.suit and self.rank == other.rank and self.hard == other.hard and self.soft == other.soft
    def __repr__( self ):
        return "{__class__.__name__}(suit={suit!r}, rank={rank!r})".format(__class__=self.__class__, **self.__dict__)
    def __str__( self ):
        return "{rank}{suit}".format(**self.__dict__)
class NumberCard( Card ):
    def _points( self ):
        return int(self.rank), int(self.rank)
class AceCard( Card ):
    insure= True
    def _points( self ):
        return 1, 11
class FaceCard( Card ):
    def _points( self ):
        return 10, 10

# We can create cards like this
# ::

d1= [ AceCard('A', '♠'), NumberCard('2','♠'), NumberCard('3','♠'), ]

# A simple class from which we can build manifest constants
# ::

class Suit:
    def __init__( self, name, symbol ):
        self.name= name
        self.symbol= symbol
    def __repr__( self ):
        return self.symbol

# Some "constants"
# ::

Club, Diamond, Heart, Spade = Suit('Club','♣'), Suit('Diamond','♦'), Suit('Heart','♥'), Suit('Spade','♠')

# We can create cards like this
# ::

d2 = [ AceCard('A', Spade), NumberCard('2', Spade), NumberCard('3', Spade), ]

# Factory Function
# ::

def card( rank, suit ):
    if rank == 1: return AceCard( 'A', suit )
    elif 2 <= rank < 11: return NumberCard( str(rank), suit )
    elif 11 <= rank < 14:
        name = { 11: 'J', 12: 'Q', 13: 'K' }[rank]
        return FaceCard( name, suit )
    raise Exception( "Design Failure" )

# This function builds a Card from a numeric rank and a Suit object. We can now # build cards very simply.
# ::

deck = [ card(rank,suit) for rank in range(1,14) for suit in (Club, Diamond, Heart, Spade) ]

# Here's a less desirable form of the factory function.
# It harbors a hidden bug because the else assumes too much.
# ::

def card2( rank, suit ):
    if rank == 1: return AceCard( 'A', suit )
    elif 2 <= rank < 11: return NumberCard( str(rank), suit )
    else:
        name = { 11: 'J', 12: 'Q', 13: 'K' }[rank]
        return FaceCard( name, suit )

try:
    deck2 = [ card2(rank,suit) for rank in range(13) for suit in (Club, Diamond, Heart, Spade) ]
except KeyError:
    pass # print( "card2 didn't work" )

# Here's a more consistent factory function that doesn't mix elif and a mapping.
# ::

def card3( rank, suit ):
    if rank == 1: return AceCard( 'A', suit )
    elif 2 <= rank < 11: return NumberCard( str(rank), suit )
    elif rank == 11:
        return FaceCard( 'J', suit )
    elif rank == 12:
        return FaceCard( 'Q', suit )
    elif rank == 13:
        return FaceCard( 'K', suit )
    else:
        raise Exception( "Rank out of range" )

deck3 = [ card3(rank,suit) for rank in range(1,14) for suit in (Club, Diamond, Heart, Spade) ]
assert deck3 == deck

# Here's an incomplete, but more consistent factory that uses just a mapping.
# This doesn't properly translate rank to a string.
# ::

def card4( rank, suit ):
    class_= {1: AceCard, 11: FaceCard, 12: FaceCard, 13: FaceCard }.get(rank, NumberCard)
    return class_( rank, suit )

deck4 = [ card4(rank,suit) for rank in range(1,14) for suit in (Club, Diamond, Heart, Spade) ]
try:
    assert deck4 == deck
    raise Exception( "Should not match!" )
except AssertionError:
    pass # Not the same

# Here's the two-parallel mapping version.
# ::

def card5( rank, suit ):
    class_= {1: AceCard, 11: FaceCard, 12: FaceCard, 13: FaceCard }.get(rank, NumberCard)
    rank_str= {1:'A', 11:'J', 12:'Q', 13:'K'}.get(rank,str(rank))
    return class_( rank_str, suit )

deck5 = [ card5(rank,suit) for rank in range(1,14) for suit in (Club, Diamond, Heart, Spade) ]
assert deck5 == deck

# Here's the mapping two a 2-tuple version.
# ::

def card6( rank, suit ):
    class_, rank_str= {
        1:(AceCard,'A'),
        11:(FaceCard,'J'),
        12:(FaceCard,'Q'),
        13:(FaceCard,'K'),
        }.get(rank, (NumberCard, str(rank)))
    return class_( rank_str, suit )

deck6 = [ card6(rank,suit) for rank in range(1,14) for suit in (Club, Diamond, Heart, Spade) ]
assert deck6 == deck

# Here's the mapping to a partial version.
# ::

from functools import partial
def card7( rank, suit ):
    part_class= {
        1:partial(AceCard,'A'),
        11:partial(FaceCard,'J'),
        12:partial(FaceCard,'Q'),
        13: partial(FaceCard,'K'),
        }.get(rank, partial(NumberCard,str(rank)))
    return part_class( suit )

deck7 = [ card7(rank,suit) for rank in range(1,14) for suit in (Club, Diamond, Heart, Spade) ]
assert deck7 == deck

# Here's a stateful card factory that's isomorphic to a partial.
# ::

class CardFactory:
    def rank( self, rank ):
        self.class_, self.rank_str= {
            1:(AceCard,'A'),
            11:(FaceCard,'J'),
            12:(FaceCard,'Q'),
            13:(FaceCard,'K'),
            }.get(rank, (NumberCard, str(rank)))
        return self
    def suit( self, suit ):
        return self.class_( self.rank_str, suit )

card8 = CardFactory()
deck8 = [ card8.rank(r+1).suit(s) for r in range(13) for s in (Club, Diamond, Heart, Spade) ]
assert deck8 == deck

# Alternative Designs for the Initialization
# =====================================================

# Subclass only
# ::

class Card2:
    def __eq__( self, other ):
        return self.suit == other.suit and self.rank == other.rank and self.hard == other.hard and self.soft == other.soft
    def __repr__( self ):
        return "suit={suit!r}, rank={rank!r}, hard={hard!r}, soft={soft!r}".format(**self.__dict__)
class NumberCard2( Card2 ):
    def  __init__( self, rank, suit ):
        self.suit= suit
        self.rank= str(rank)
        self.hard = self.soft = rank
class AceCard2( Card2 ):
    def  __init__( self, rank, suit ):
        self.suit= suit
        self.rank= "A"
        self.hard, self.soft =  1, 11
class FaceCard2( Card2 ):
    def  __init__( self, rank, suit ):
        self.suit= suit
        self.rank= {11: 'J', 12: 'Q', 13: 'K' }[rank]
        self.hard = self.soft = 10

def card9( rank, suit ):
    if rank == 1: return AceCard2( rank, suit )
    elif 2 <= rank < 11: return NumberCard2( rank, suit )
    elif 11 <= rank < 14: return FaceCard2( rank, suit )
    else:
        raise Exception( "Rank out of range" )

deck9 = [ card9(rank,suit) for rank in range(1,14) for suit in (Club, Diamond, Heart, Spade) ]
for c9, c in zip( deck9, deck ):
    assert c9 == c, "{0!r} != {1!r}".format(c9,c)
assert deck9 == deck

# Mixed subclass and superclass.
# ::

class Card3:
    def __init__( self, rank, suit, hard, soft ):
        self.rank= rank
        self.suit= suit
        self.hard= hard
        self.soft= soft
    def __eq__( self, other ):
        return self.suit == other.suit and self.rank == other.rank and self.hard == other.hard and self.soft == other.soft
class NumberCard3( Card3 ):
    def  __init__( self, rank, suit ):
        super().__init__( str(rank), suit, rank, rank )
class AceCard3( Card3 ):
    def  __init__( self, rank, suit ):
        super().__init__( "A", suit, 1, 11 )
class FaceCard3( Card3 ):
    def  __init__( self, rank, suit ):
        super().__init__( {11: 'J', 12: 'Q', 13: 'K' }[rank], suit, 10, 10 )

def card10( rank, suit ):
    if rank == 1: return AceCard3( rank, suit )
    elif 2 <= rank < 11: return NumberCard3( rank, suit )
    elif 11 <= rank < 14: return FaceCard3( rank, suit )
    else:
        raise Exception( "Rank out of range" )

deck10 = [ card10(rank,suit) for rank in range(1,14) for suit in (Club, Diamond, Heart, Spade) ]
assert deck10 == deck

# Composite Objects: Deck
# ====================================

# Need this
# ::

import random

# A simple Deck definition
# ::

class Deck:
    def __init__( self ):
        self._cards = [ card6(r+1,s) for r in range(13) for s in (Club, Diamond, Heart, Spade) ]
        random.shuffle( self._cards )
    def pop( self ):
        return self._cards.pop()

d= Deck()
hand= [ d.pop(), d.pop() ]

print( hand )

# A subclass of list definition
# ::

class Deck2( list ):
    def __init__( self ):
        super().__init__( card6(r+1,s) for r in range(13) for s in (Club, Diamond, Heart, Spade) )
        random.shuffle( self )

d= Deck2()
hand= [ d.pop(), d.pop() ]

print( hand )

# A better subclass of list which has the necessary additional features of
# multiple sets of cards plus not dealing the entire deck.
# ::

class Deck3(list):
    def __init__(self, decks=1):
        super().__init__()
        for i in range(decks):
            self.extend( card6(r+1,s) for r in range(13) for s in (Club, Diamond, Heart, Spade) )
        random.shuffle( self )
        burn= random.randint(1,52)
        for i in range(burn): self.pop()

d= Deck3()
hand= [ d.pop(), d.pop() ]

print( hand )


# Composite Objects: Hand
# ===================================

# A simplistic Hand without a proper initialization of the cards.
# ::

class Hand:
    def __init__( self, dealer_card ):
        self.dealer_card= dealer_card
        self.cards= []
    def hard_total(self ):
        return sum(c.hard for c in self.cards)
    def soft_total(self ):
        return sum(c.soft for c in self.cards)

d = Deck()
h = Hand( d.pop() )
h.cards.append( d.pop() )
h.cards.append( d.pop() )

# A Better Hand with a complete initialization of the cards.
# This works better with serialization.
# ::

class Hand2:
    def __init__( self, dealer_card, *cards ):
        self.dealer_card= dealer_card
        self.cards = list(cards)
    def card_append( self, card ):
        self.cards.append( card )
    def hard_total(self ):
        return sum(c.hard for c in self.cards)
    def soft_total(self ):
        return sum(c.soft for c in self.cards)

d = Deck()
h = Hand2( d.pop(), d.pop(), d.pop() )

# A Hand which can be built from another hand. This allows us to freeze
# the hand or build a memento version of the hand.
# ::

class Hand3:
    def __init__( self, *args, **kw ):
        if len(args) == 1 and isinstance(args[0],Hand3):
            # Clone an existing hand
            other= args[0]
            self.dealer_card= other.dealer_card
            self.cards= other.cards
        else:
            # Build a fresh, new hand.
            dealer_card, *cards = args
            self.dealer_card=  dealer_card
            self.cards= list(cards)

d = Deck()
h = Hand3( d.pop(), d.pop(), d.pop() )
memento = Hand3( h )

# A Hand which can be built from another hand. This can also be used to
# split a hand.
# ::

class Hand4:
    def __init__( self, *args, **kw ):
        if len(args) == 1 and isinstance(args[0],Hand4):
            # Clone an existing hand
            other= args[0]
            self.dealer_card= other.dealer_card
            self.cards= other.cards
        elif len(args) == 2 and isinstance(args[0],Hand4) and 'split' in kw:
            # Split an existing hand
            other, card= args
            self.dealer_card= other.dealer_card
            self.cards= [other.cards[kw['split']], card]
        elif len(args) == 3:
            # Build a fresh, new hand.
            dealer_card, *cards = args
            self.dealer_card=  dealer_card
            self.cards= list(cards)
        else:
            raise TypeError( "Invalid constructor args={0!r} kw={1!r}".format(args, kw) )
    def __str__( self ):
        return ", ".join( map(str, self.cards) )

d = Deck()
h = Hand4( d.pop(), d.pop(), d.pop() )
s1 = Hand4( h, d.pop(), split=0 )
s2 = Hand4( h, d.pop(), split=1 )
print( "start", h, "split1", s1, "split2", s2 )

# A Hand with static methods to split or frozen as a memento.
# ::

class Hand5:
    def __init__( self, dealer_card, *cards ):
        self.dealer_card= dealer_card
        self.cards = list(cards)
    @staticmethod
    def freeze( other ):
        hand= Hand5( other.dealer_card, *other.cards )
        return hand
    @staticmethod
    def split( other, card0, card1 ):
        hand0= Hand5( other.dealer_card, other.cards[0], card0 )
        hand1= Hand5( other.dealer_card, other.cards[1], card1 )
        return hand0, hand1
    def __str__( self ):
        return ", ".join( map(str, self.cards) )

d = Deck()
h = Hand5( d.pop(), d.pop(), d.pop() )
s1, s2 = Hand5.split( h, d.pop(), d.pop() )
print( "start", h, "split1", s1, "split2", s2 )

# Composite Objects: Betting Strategy
# ==============================================

# A strategy class hierarchy for Betting.
# ::

class BettingStrategy:
    def bet( self ):
        raise NotImplementedError( "No bet method" )
    def record_win( self ):
        pass
    def record_loss( self ):
        pass

class Flat(BettingStrategy):
    def bet( self ):
        return 1

flat_bet= Flat()

flat_bet.bet()

import abc
from abc import abstractmethod
class BettingStrategy2(metaclass=abc.ABCMeta):
    @abstractmethod
    def bet( self ):
        return 1
    def record_win( self ):
        pass
    def record_loss( self ):
        pass

# A strategy class hierarchy for Play.
# ::

class GameStrategy:
    def insurance( self, hand ):
        return False
    def split( self, hand ):
        return False
    def double( self, hand ):
        return False
    def hit( self, hand ):
        return sum(c.hard for c in hand.cards) <= 17

dumb = GameStrategy()

# A simple outline for the Table.
# ::

class Table:
    def __init__( self ):
        self.deck = Deck()
    def place_bet( self, amount ):
        print( "Bet", amount )
    def get_hand( self ):
        try:
            self.hand= Hand2( d.pop(), d.pop(), d.pop() )
            self.hole_card= d.pop()
        except IndexError:
            # Out of cards: need to shuffle.
            # This is not technically correct.
            self.deck= Deck()
            return self.get_hand()
        print( "Deal", self.hand )
        return self.hand
    def can_insure( self, hand ):
        return hand.dealer_card.insure

# A Player definition
# ::

class Player:
    def __init__( self, table, bet_strategy, game_strategy ):
        self.bet_strategy = bet_strategy
        self.game_strategy = game_strategy
        self.table= table
    def game( self ):
        self.table.place_bet( self.bet_strategy.bet() )
        self.hand= self.table.get_hand()
        if self.table.can_insure( self.hand ):
            if self.game_strategy.insurance( self.hand ):
                self.table.insure( self.bet_strategy.bet() )
        # etc.

# Typical Use Case
# ::

table = Table()
flat_bet= Flat()
dumb = GameStrategy()
p = Player( table, flat_bet, dumb )
p.game()

# A Player definition using wide-open keyword definitions.
# ::

class Player2( Player ):
    def __init__( self, **kw ):
        """Must provide table, bet_strategy, game_strategy."""
        self.__dict__.update( kw )
    def game( self ):
        self.table.place_bet( self.bet_strategy.bet() )
        self.hand= self.table.get_hand()

# Typical Use Case.
# ::

table = Table()
flat_bet= Flat()
dumb = GameStrategy()
p1 = Player2( table=table, bet_strategy=flat_bet, game_strategy=dumb )
p1.game()

# Bonus Use Case. Set an additional attribute.
# ::

p2 = Player2( table=table, bet_strategy=flat_bet, game_strategy=dumb, log_name="Flat/Dumb" )
p2.game()
print( p2.log_name, p2.hand )

# A Player definition using wide-open keyword definitions.
# ::

class Player3( Player ):
    def __init__( self, table, bet_strategy, game_strategy, **extras ):
        self.bet_strategy = bet_strategy
        self.game_strategy = game_strategy
        self.table= table
        self.__dict__.update( extras )

table = Table()
flat_bet= Flat()
dumb = GameStrategy()
p3 = Player3( table, flat_bet, dumb, log_name="Flat/Dumb" )
p3.game()
print( p3.log_name, p3.hand )

# Bad Ideas
# ====================

# Validation
# ::

class ValidPlayer:
    def __init__( self, table, bet_strategy, game_strategy ):
        assert isinstance( table, Table )
        assert isinstance( bet_strategy, BettingStrategy )
        assert isinstance( game_strategy, GameStrategy )

        self.bet_strategy = bet_strategy
        self.game_strategy = game_strategy
        self.table= table

table = Table()
flat_bet= Flat()
dumb = GameStrategy()
p4= ValidPlayer( table, flat_bet, dumb )

class Player:
    def __init__( self, table, bet_strategy, game_strategy ):
        """Creates a new player associated with a table, and configured with
        proper betting and play strategies

        :param table: an instance of :class:`Table`
        :param bet_strategy: an instance of :class:`BettingStrategy`
        :param  game_strategy: an instance of :class:`GameStrategy`
        """
        self.bet_strategy = bet_strategy
        self.game_strategy = game_strategy
        self.table= table
