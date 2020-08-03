#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Chapter 15 -- Testing
# --------------------------------------------

# ..  sectnum::
#
# ..  contents::
#

# Card and Deck
# ========================

import random

class Card:
    def __init__( self, rank, suit, hard=None, soft=None ):
        self.rank= rank
        self.suit= suit
        self.hard= hard or int(rank)
        self.soft= soft or int(rank)
    def __str__( self ):
        return "{0.rank!s}{0.suit!s}".format(self)

class AceCard( Card ):
    def __init__( self, rank, suit ):
        super().__init__( rank, suit, 1, 11 )

class FaceCard( Card ):
    def __init__( self, rank, suit ):
        super().__init__( rank, suit, 10, 10 )

class LogicError( Exception ):
    pass

def card( rank, suit ):
    if rank == 1: return AceCard( rank, suit )
    elif 2 <= rank < 11: return Card( rank, suit )
    elif 11 <= rank < 14: return FaceCard( rank, suit )
    else: raise Exception( "LogicError" )

Suits = '♣', '♦', '♥', '♠'
class Deck1( list ):
    def __init__( self, size=1 ):
        super().__init__()
        self.rng= random.Random()
        for d in range(size):
            for s in Suits:
                cards = ([AceCard(1, s)]
                + [Card(r, s) for r in range(2, 12)]
                + [FaceCard(r, s) for r in range(12, 14)])
                super().extend( cards )
        self.rng.shuffle( self )

class Deck2( list ):
    def __init__( self, size=1,
        random=random.Random(),
        ace_class=AceCard, card_class=Card, face_class=FaceCard ):
        super().__init__()
        self.rng= random
        for d in range(size):
            for s in Suits:
                cards =  ([ace_class(1, s)]
                + [ card_class(r, s) for r in range(2, 12) ]
                + [ face_class(r, s) for r in range(12, 14) ] )
                super().extend( cards )
        self.rng.shuffle( self )

# Card Test
# ========================

# Some Test Cases
# ::

import unittest

class TestCard( unittest.TestCase ):
    def setUp( self ):
        self.three_clubs= Card( 3, '♣' )
    def test_should_returnStr( self ):
        self.assertEqual( "3♣", str(self.three_clubs) )
    def test_should_getAttrValues( self ):
        self.assertEqual( 3, self.three_clubs.rank )
        self.assertEqual( "♣", self.three_clubs.suit )
        self.assertEqual( 3, self.three_clubs.hard )
        self.assertEqual( 3, self.three_clubs.soft )

class TestAceCard( unittest.TestCase ):
    def setUp( self ):
        self.ace_spades= AceCard( 1, '♠' )
    def test_should_returnStr( self ):
        self.assertEqual( "A♠", str(self.ace_spades) )
    def test_should_getAttrValues( self ):
        self.assertEqual( 1, self.ace_spades.rank )
        self.assertEqual( "♠", self.ace_spades.suit )
        self.assertEqual( 1, self.ace_spades.hard )
        self.assertEqual( 11, self.ace_spades.soft )

class TestFaceCard( unittest.TestCase ):
    def setUp( self ):
        self.queen_hearts= FaceCard( 12, '♥' )
    def test_should_returnStr( self ):
        self.assertEqual( "Q♥", str(self.queen_hearts) )
    def test_should_getAttrValues( self ):
        self.assertEqual( 12, self.queen_hearts.rank )
        self.assertEqual( "♥", self.queen_hearts.suit )
        self.assertEqual( 10, self.queen_hearts.hard )
        self.assertEqual( 10, self.queen_hearts.soft )

# Suite
# ::

def suite2():
    s= unittest.TestSuite()
    load_from= unittest.defaultTestLoader.loadTestsFromTestCase
    s.addTests( load_from(TestCard) )
    s.addTests( load_from(TestAceCard) )
    s.addTests( load_from(TestFaceCard) )
    return s

if __name__ == "__main__":
    t= unittest.TextTestRunner()
    t.run( suite2() )

# Card Factory Test
# =============================

# Another Test Case
# ::

class TestCardFactory( unittest.TestCase ):
    def test_rank1_should_createAceCard( self ):
        c = card( 1, '♣' )
        self.assertIsInstance( c, AceCard )
    def test_rank2_should_createCard( self ):
        c = card( 2, '♦' )
        self.assertIsInstance( c, Card )
    def test_rank10_should_createCard( self ):
        c = card( 10, '♥' )
        self.assertIsInstance( c, Card )
    def test_rank10_should_createFaceCard( self ):
        c = card( 11, '♠' )
        self.assertIsInstance( c, Card )
    def test_rank13_should_createFaceCard( self ):
        c = card( 13, '♣' )
        self.assertIsInstance( c, Card )
    def test_otherRank_should_exception( self ):
        with self.assertRaises( LogicError ):
            c = card(14, '♦')
        with self.assertRaises( LogicError ):
            c = card(0, '♦')

# Another Suite
# :

def suite3():
    s= unittest.TestSuite()
    s.addTests( unittest.defaultTestLoader.loadTestsFromTestCase(TestCardFactory) )
    return s

if __name__ == "__main__":
    t= unittest.TextTestRunner()
    t.run( suite3() )

# Deck with Mock Card
# ==============================

# Class Definitios
# ::

class DeckEmpty(Exception): pass

class Deck3( list ):
    def __init__( self, size=1,
        random=random.Random(),
        card_factory=card ):
        super().__init__()
        self.rng= random
        for d in range(size):
            super().extend(
                 card_factory(r,s) for r in range(1,13) for s in Suits )
        self.rng.shuffle( self )
    def deal( self ):
        try:
            return self.pop(0)
        except IndexError:
            raise DeckEmpty()

# Test Cases
# ::

import unittest
import unittest.mock

class TestDeckBuild( unittest.TestCase ):
    def setUp( self ):
        self.test_card= unittest.mock.Mock( return_value=unittest.mock.sentinel )
        self.test_rng= random.Random()
        self.test_rng.shuffle= unittest.mock.Mock( return_value=None )
    def test_deck_1_should_build(self):
        d= Deck3( size=1, random=self.test_rng, card_factory= self.test_card )
        self.assertEqual( 52*[unittest.mock.sentinel], d )
        self.test_rng.shuffle.assert_called_with( d )
        self.assertEqual( 52, len(self.test_card.call_args_list) )
        expected = [
            unittest.mock.call(r,s)
                for r in range(1,14)
                    for s in ('♣', '♦', '♥', '♠') ]
        self.assertEqual( expected, self.test_card.call_args_list )

class TestDeckDeal( unittest.TestCase ):
    def setUp( self ):
        self.test_card= unittest.mock.Mock( side_effect=range(52) )
        self.test_rng= random.Random()
        self.test_rng.shuffle= unittest.mock.Mock( return_value=None )
    def test_deck_1_should_deal( self ):
        d= Deck3( size=1, random=self.test_rng, card_factory= self.test_card )
        dealt = []
        for c in range(52):
            c= d.deal()
            dealt.append(c)
        self.assertEqual( dealt, list(range(52)) )
    def test_empty_deck_should_exception( self ):
        d= Deck3( size=1, random=self.test_rng, card_factory= self.test_card )
        for c in range(52):
            c= d.deal()
        self.assertRaises( DeckEmpty, d.deal )

# Suite
# ::

def suite4():
    s= unittest.TestSuite()
    s.addTests( unittest.defaultTestLoader.loadTestsFromTestCase(TestDeckBuild) )
    s.addTests( unittest.defaultTestLoader.loadTestsFromTestCase(TestDeckDeal) )
    return s

if __name__ == "__main__":
    t= unittest.TextTestRunner()
    t.run( suite4() )

# Doctest
# ===============

# Sample Function with doctest string
# ::

def ackermann( m, n ):
    """Ackermann's Function
    ackermann( m, n ) -> 2↑^{m-2}(n+3) - 3.

    See http://en.wikipedia.org/wiki/Ackermann_function and
    http://en.wikipedia.org/wiki/Knuth%27s_up-arrow_notation.

    >>> from p3_c15 import ackermann
    >>> ackermann(2,4)
    11
    >>> ackermann(0,4)
    5
    >>> ackermann(1,0)
    2
    >>> ackermann(1,1)
    3

    """
    if m == 0: return n+1
    elif m > 0 and n == 0: return ackermann( m-1, 1 )
    elif m > 0 and n > 0: return ackermann( m-1, ackermann( m, n-1 ) )

if __name__ == "__main__":
    import doctest
    suite5= doctest.DocTestSuite()
    t= unittest.TextTestRunner(verbosity=2)
    t.run( suite5 )


# Combined Testing
# =========================

# Main Program to combine suites
# ::

if __name__ == "__main__":
    all_tests= unittest.TestSuite()
    all_tests.addTests( suite2() )
    all_tests.addTests( suite3() )
    all_tests.addTests( suite4() )
    all_tests.addTests( suite5 )
    t= unittest.TextTestRunner()
    t.run( all_tests )

# OS testing
# ======================

# Functions to test
# ::

from collections import namedtuple, defaultdict
GameStat = namedtuple( "GameStat", "player,bet,rounds,final" )

import csv
def gamestat_iter(iterator):
    for row in iterator:
        yield GameStat( row['player'], row['bet'], int(row['rounds']), int(row['final']) )

def rounds_final( name="p2_c09_blackjack.csv" ):
    stats= defaultdict(list)
    with open(name, "r", newline="") as source:
        reader= csv.DictReader( source )
        assert set(reader.fieldnames) == set(GameStat._fields)
        for gs in gamestat_iter(reader):
            stats[gs.rounds].append( gs.final )
    return stats

# Two approaches:
#
# - io.StringIO()
#
# - create a file

# We might want to test missing or damaged file features, in which
# case StringIO doesn't work as well as creating a file.

# Test Cases
# ::

import os
class Test_Missing( unittest.TestCase ):
    def setUp( self ):
        try:
            os.remove( "p3_c15_sample.csv" )
            #print( "setUp removed p3_c15_sample.csv" )
        except OSError as e:
            pass
            #print("setUp expected", e)
    def test_missingFile_should_returnDefault( self ):
        self.assertRaises( FileNotFoundError, rounds_final,  "p3_c15_sample.csv", )

class Test_Damaged( unittest.TestCase ):
    def setUp( self ):
        with open(  "p3_c15_sample.csv", "w" ) as target:
            print( "not_player,bet,rounds,final", file=target )
            print( "data,1,1,1", file=target )
    def test_damagedFile_should_raiseException( self ):
        stats= rounds_final( "p3_c15_sample.csv" )
        self.assertEqual( 0, len(stats) )

def suite7():
    s= unittest.TestSuite()
    s.addTests( unittest.defaultTestLoader.loadTestsFromTestCase(Test_Missing) )
    s.addTests( unittest.defaultTestLoader.loadTestsFromTestCase(Test_Damaged) )
    return s

if __name__ == "__main__":
    t= unittest.TextTestRunner()
    t.run( suite7() )

# SQLite testing
# =========================

# SQLAlchemy ORM classes
# ::

from p2_c11 import Base, Blog, Post, Tag, assoc_post_tag
import datetime

# Create Test Database and Schema
# ::

import sqlalchemy.exc
from sqlalchemy import create_engine

def built_test_db( name='sqlite:///./p3_c15_blog.db' ):
    engine = create_engine(name, echo=True)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    return engine

# Unittest Case
# ::

from sqlalchemy.orm import sessionmaker
class Test_Blog_Queries( unittest.TestCase ):
    @staticmethod
    def setUpClass():
        engine= built_test_db()
        Test_Blog_Queries.Session = sessionmaker(bind=engine)
        session= Test_Blog_Queries.Session()

        tag_rr= Tag( phrase="#RedRanger" )
        session.add( tag_rr )
        tag_w42= Tag( phrase="#Whitby42" )
        session.add( tag_w42 )
        tag_icw= Tag( phrase="#ICW" )
        session.add( tag_icw )
        tag_mis= Tag( phrase="#Mistakes" )
        session.add( tag_mis )

        blog1= Blog( title="Travel 2013" )
        session.add( blog1 )
        b1p1= Post( date=datetime.datetime(2013,11,14,17,25),
            title="Hard Aground",
            rst_text="""Some embarrassing revelation. Including ☹ and ⚓︎""",
            blog=blog1,
            tags=[tag_rr, tag_w42, tag_icw],
            )
        session.add(b1p1)
        b1p2= Post( date=datetime.datetime(2013,11,18,15,30),
            title="Anchor Follies",
            rst_text="""Some witty epigram. Including ☺ and ☀︎︎""",
            blog=blog1,
            tags=[tag_rr, tag_w42, tag_mis],
            )
        session.add(b1p2)

        blog2= Blog( title="Travel 2014" )
        session.add( blog2 )
        session.commit()

    def setUp( self ):
        self.session= Test_Blog_Queries.Session()
    def test_query_eqTitle_should_return1Blog( self ):
        """Tests schema definition"""
        results= self.session.query( Blog ).filter(
            Blog.title == "Travel 2013" ).all()
        self.assertEqual( 1, len(results) )
        self.assertEqual( 2, len(results[0].entries) )
    def test_query_likeTitle_should_return2Blog( self ):
        """Tests SQLAlchemy, and test data"""
        results= self.session.query( Blog ).filter(
            Blog.title.like("Travel %") ).all()
        self.assertEqual( 2, len(results) )
    def test_query_eqW42_tag_should_return2Post( self ):
        results= self.session.query(Post)\
        .join(assoc_post_tag).join(Tag).filter(
            Tag.phrase == "#Whitby42" ).all()
        self.assertEqual( 2, len(results) )
    def test_query_eqICW_tag_should_return1Post( self ):
        results= self.session.query(Post)\
        .join(assoc_post_tag).join(Tag).filter(
            Tag.phrase == "#ICW" ).all()
        #print( [r.title for r in results] )
        self.assertEqual( 1, len(results) )
        self.assertEqual( "Hard Aground", results[0].title )
        self.assertEqual( "Travel 2013", results[0].blog.title )
        self.assertEqual( set(["#RedRanger", "#Whitby42", "#ICW"]), set(t.phrase for t in results[0].tags) )

# Make a suite of the testcases
# ::

def suite8():
    s= unittest.TestSuite()
    s.addTests( unittest.defaultTestLoader.loadTestsFromTestCase(Test_Blog_Queries) )
    return s

if __name__ == "__main__":
    t= unittest.TextTestRunner()
    t.run( suite8() )

# External CSV Examples
# ======================

# Unit Under Test
# ::

from p1_c03 import RateTimeDistance

# Sample data
# ::

sample_data = """\
rate_in,time_in,distance_in,rate_out,time_out,distance_out
2,3,,2,3,6
5,,7,5,1.4,7
,11,13,1.18,11,13
"""

# Parse the sample data
# ::

def float_or_none( text ):
    if len(text) == 0: return None
    return float(text)

# TestCase with only one test method
# ::

class Test_RTD( unittest.TestCase ):
    def __init__( self, rate_in,time_in,distance_in,
        rate_out,time_out,distance_out ):
        super().__init__()
        self.args = dict( rate=float_or_none(rate_in),
            time=float_or_none(time_in),
            distance=float_or_none(distance_in) )
        self.result= dict( rate=float_or_none(rate_out),
            time=float_or_none(time_out),
            distance=float_or_none(distance_out) )
    def shortDescription( self ):
        return "{0} -> {1}".format(self.args, self.result)
    def setUp( self ):
        self.rtd= RateTimeDistance( **self.args )
    def runTest( self ):
        self.assertAlmostEqual( self.rtd.distance, self.rtd.rate*self.rtd.time )
        self.assertAlmostEqual( self.rtd.rate, self.result['rate'] )
        self.assertAlmostEqual( self.rtd.time, self.result['time'] )
        self.assertAlmostEqual( self.rtd.distance, self.result['distance'] )

# Build Suite from user-supplied sample data
# ::

with open("p3_c15_data.csv","w",newline="") as target:
    target.write( sample_data )

import csv
def suite9():
    suite= unittest.TestSuite()
    with open("p3_c15_data.csv","r",newline="") as source:
        rdr= csv.DictReader( source )
        for row in rdr:
            suite.addTest( Test_RTD(**row) )
    return suite

if __name__ == "__main__":
    t= unittest.TextTestRunner()
    t.run( suite9() )

# Performance Testing
# ======================

import unittest
import timeit
class Test_Performance( unittest.TestCase ):
    def test_simpleCalc_shouldbe_fastEnough( self ):
        t= timeit.timeit(
        stmt="""RateTimeDistance( rate=1, time=2 )""",
        setup="""from p1_c03 import RateTimeDistance"""
        )
        print( "Run time", t )
        self.assertLess( t, 10, "run time {0} >= 10".format(t) )

# Make a suite of the testcases
# ::

def suite10():
    s= unittest.TestSuite()
    s.addTests( unittest.defaultTestLoader.loadTestsFromTestCase(Test_Performance) )
    return s

if __name__ == "__main__":
    t= unittest.TextTestRunner()
    t.run( suite10() )

