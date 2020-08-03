#!/usr/bin/env python3

# Chapter 9 -- Simple Persistence: JSON, YAML, Pickle, CSV and XML
# -----------------------------------------------------------------

# ..  sectnum::
#
# ..  contents::
#

# Persistence Classes
# ========================================

# A detail class for micro-blog posts
# ::

import datetime
class Post:
    def __init__( self, date, title, rst_text, tags ):
        self.date= date
        self.title= title
        self.rst_text= rst_text
        self.tags= tags
    def as_dict( self ):
        return dict(
            date= str(self.date),
            title= self.title,
            underline= "-"*len(self.title),
            rst_text= self.rst_text,
            tag_text= " ".join(self.tags),
        )

# Here's a collection of these posts. This is an extension
# of list which doesn't work well with JSON.
# ::

from collections import defaultdict
class Blog_x( list ):
    def __init__( self, title, posts=None ):
        self.title= title
        super().__init__( posts if posts is not None else [] )
    def by_tag(self):
        tag_index= defaultdict(list)
        for post in self:
            for tag in post.tags:
                tag_index[tag].append( post )
        return tag_index
    def as_dict( self ):
        return dict(
            title= self.title,
            entries= [p.as_dict() for p in self],
        )

# An example blog
# ::

travel_x = Blog_x( "Travel" )
travel_x.append(
    Post( date=datetime.datetime(2013,11,14,17,25),
        title="Hard Aground",
        rst_text="""Some embarrassing revelation. Including ☹ and ⚓""",
        tags=("#RedRanger", "#Whitby42", "#ICW"),
        )
)
travel_x.append(
    Post( date=datetime.datetime(2013,11,18,15,30),
        title="Anchor Follies",
        rst_text="""Some witty epigram. Including < & > characters.""",
        tags=("#RedRanger", "#Whitby42", "#Mistakes"),
        )
)

# JSON
# ================================

# Example 1: Simple
# ####################

# Simple JSON dump
# ::

import json

if __name__=="__main__":
    print( "Less Elegant" )
    print( json.dumps(travel_x.as_dict(), indent=4) )

# Example 2. JSON: Flawed Design
# ###############################

# Flawed Encoder based on flowed design of the class.
# ::

def blogx_encode( object ):
    if isinstance(object, datetime.datetime):
        return dict(
            __class__= "datetime.datetime",
            __args__= [],
            __kw__= dict(
                year= object.year,
                month= object.month,
                day= object.day,
                hour= object.hour,
                minute= object.minute,
                second= object.second,
            )
        )
    elif isinstance(object, Post):
        return dict(
            __class__= "Post",
            __args__= [],
            __kw__= dict(
                date= object.date,
                title= object.title,
                rst_text= object.rst_text,
                tags= object.tags,
            )
        )
    elif isinstance(object, Blog_x):
        return dict(
            __class__= "Blog_x",
            __args__= [],
            __kw__= dict(
                title= object.title,
                entries= tuple(object),
            )
        )
    else:
        return super().default(o)

def blogx_decode( some_dict ):
    if set(some_dict.keys()) == set( ["__class__", "__args__", "__kw__"] ):
        class_= eval(some_dict['__class__'])
        return class_( *some_dict['__args__'], **some_dict['__kw__'] )
    else:
        return some_dict

# Problem: The Blog entries vanished.
# ::

if __name__=="__main__":

    print( "Damaged" )
    text= json.dumps(travel_x, indent=4, default=blogx_encode)
    print( text )
    copy= json.loads(text, object_hook= blogx_decode)

# Example 3 JSON: Better Design
# ###############################

# Consider this wrapped version instead of an extended version

# Here's another collection of these posts. This
# wraps a list which works much better with JSON than extending a list.
# ::

import datetime
from collections import defaultdict
class Blog:
    def __init__( self, title, posts=None ):
        self.title= title
        self.entries= posts if posts is not None else []
    def append( self, post ):
        self.entries.append(post)
    def by_tag(self):
        tag_index= defaultdict(list)
        for post in self.entries:
            for tag in post.tags:
                tag_index[tag].append( post.as_dict() )
        return tag_index
    def as_dict( self ):
        return dict(
            title= self.title,
            underline= "="*len(self.title),
            entries= [p.as_dict() for p in self.entries],
        )

# An example blog
# ::

travel = Blog( "Travel" )
travel.append(
    Post( date=datetime.datetime(2013,11,14,17,25),
        title="Hard Aground",
        rst_text="""Some embarrassing revelation. Including ☹ and ⚓︎""",
        tags=("#RedRanger", "#Whitby42", "#ICW"),
        )
)
travel.append(
    Post( date=datetime.datetime(2013,11,18,15,30),
        title="Anchor Follies",
        rst_text="""Some witty epigram. Including < & > characters.""",
        tags=("#RedRanger", "#Whitby42", "#Mistakes"),
        )
)

def blog_encode( object ):
    if isinstance(object, datetime.datetime):
        return dict(
            __class__= "datetime.datetime",
            __args__= [],
            __kw__= dict(
                year= object.year,
                month= object.month,
                day= object.day,
                hour= object.hour,
                minute= object.minute,
                second= object.second,
            )
        )
    elif isinstance(object, Post):
        return dict(
            __class__= "Post",
            __args__= [],
            __kw__= dict(
                date= object.date,
                title= object.title,
                rst_text= object.rst_text,
                tags= object.tags,
            )
        )
    elif isinstance(object, Blog):
        return dict(
            __class__= "Blog",
            __args__= [
                object.title,
                object.entries,
            ],
            __kw__= {}
        )
    else:
        return json.JSONEncoder.default(o)

def blog_decode( some_dict ):
    if set(some_dict.keys()) == set( ["__class__", "__args__", "__kw__"] ):
        class_= eval(some_dict['__class__'])
        return class_( *some_dict['__args__'], **some_dict['__kw__'] )
    else:
        return some_dict

if __name__=="__main__":

    print( "Better" )
    text= json.dumps(travel, indent=4, default=blog_encode)
    print( text )
    copy= json.loads(text, object_hook= blog_decode)

# Sidebar: Demo of rendering 1
# ###############################

# Here's a template for an individual post
# ::

import string

# Here's a way to render the entire blog in RST
# ::

def render( blog ):
    post= string.Template( """
    $title
    $underline

    $rst_text

    :date: $date

    :tags: $tag_text
    """)

    # with redirect_stdout("some_file"):
    print( "{title}\n{underline}\n".format(**blog.as_dict()) )
    for p in blog.entries:
        print( post.substitute( **p.as_dict() ) )

    tag_index= blog.by_tag()
    print( "Tag Index" )
    print( "=========" )
    print()
    for tag in tag_index:
        print( "*   {0}".format(tag) )
        print()
        for post_dict in tag_index[tag]:
            print( "    -   `{title}`_".format(**post_dict) )
        print()

render(travel)

# Sidebar: Demo of rendering 2 (using Jinja2)
# ############################################

try:
    from jinja2 import Template
    blog_template= Template( """
{{title}}
{{underline}}

{% for e in entries %}
{{e.title}}
{{e.underline}}

{{e.rst_text}}

:date: {{e.date}}

:tags: {{e.tag_text}}
{% endfor %}

Tag Index
=========
{% for t in tags %}

*   {{t}}
    {% for post in tags[t] %}

    -   `{{post.title}}`_
    {% endfor %}
{% endfor %}
""")
    print( blog_template.render( tags=travel.by_tag(), **travel.as_dict() ) )
    #import sys
    #sys.exit(0)

except ImportError as e:
    print( e )

# Example 4. JSON: Refactoring Encoding
# ######################################

# Changes to the class definitions
# ::

class Blog_J( Blog ):
    @property
    def _json( self ):
        return dict( __class__= self.__class__.__name__,
            __kw__= {},
            __args__= [ self.title, self.entries ]
        )

class Post_J( Post ):
    @property
    def _json( self ):
        return dict(
            __class__= self.__class__.__name__,
            __kw__= dict(
                date= self.date,
                title= self.title,
                rst_text= self.rst_text,
                tags= self.tags,
            ),
            __args__= []
        )

def blog_j_encode( object ):
    if isinstance(object, datetime.datetime):
        return dict(
            __class__= "datetime.datetime",
            __args__= [],
            __kw__= dict(
                year= object.year,
                month= object.month,
                day= object.day,
                hour= object.hour,
                minute= object.minute,
                second= object.second,
            )
        )
    else:
        try:
            encoding= object._json
        except AttributeError:
            encoding= json.JSONEncoder.default(o)
        return encoding

travel3 = Blog_J( "Travel" )
travel3.append(
    Post_J( date=datetime.datetime(2013,11,14,17,25),
        title="Hard Aground",
        rst_text="""Some embarrassing revelation. Including ☹ and ⚓""",
        tags=("#RedRanger", "#Whitby42", "#ICW"),
        )
)
travel3.append(
    Post_J( date=datetime.datetime(2013,11,18,15,30),
        title="Anchor Follies",
        rst_text="""Some witty epigram.""",
        tags=("#RedRanger", "#Whitby42", "#Mistakes"),
        )
)

if __name__=="__main__":
    print( "Best" )
    text= json.dumps(travel3, indent=4, default=blog_j_encode)
    print( text )

# Example 5: JSON: Better Date Encoding
# ######################################

# Changes to the class definitions
# ::

def blog_j2_encode( object ):
    if isinstance(object, datetime.datetime):
        return dict(
            __class__= "datetime.datetime.strptime",
            __args__= [
                object.strftime("%Y-%m-%dT%H:%M:%S"),
                "%Y-%m-%dT%H:%M:%S",
            ],
            __kw__= {}
        )
    else:
        try:
            encoding= object._json
        except AttributeError:
            encoding= json.JSONEncoder.default(o)
        return encoding

if __name__=="__main__":
    print( "Best" )
    text= json.dumps(travel3, indent=4, default=blog_j2_encode)
    print( text )
    copy= json.loads(text, object_hook= blog_decode)

with open("p2_c09.json", "w", encoding="UTF-8") as target:
    json.dump( travel3, target, separators=(',', ':'), default=blog_j2_encode )

# YAML
# ===================

# Example 1: That's it.
# ######################

# Start with original defintions
# ::

import yaml

if __name__=="__main__":
    text= yaml.dump(travel)
    print( text )
    copy= yaml.load(text)
    print( type(copy), copy.title )
    for p in copy.entries:
        print( p.date.year, p.date.month, p.date.day, p.title, p.tags )

    text2= yaml.dump(travel, allow_unicode=True )
    print( text2 )

with open("p2_c09.yaml", "w", encoding="UTF-8") as target:
    yaml.dump( travel, target )

# Example 2: Cards
# ###################

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

deck = [ AceCard('A','♣'), Card('2','♥'), FaceCard('K','♦') ]

if __name__=="__main__":
    text= yaml.dump( deck, allow_unicode=True )
    print( text )

def card_representer(dumper, card):
    return dumper.represent_scalar('!Card',
    "{0.rank!s}{0.suit!s}".format(card) )
def acecard_representer(dumper, card):
    return dumper.represent_scalar('!AceCard',
    "{0.rank!s}{0.suit!s}".format(card) )
def facecard_representer(dumper, card):
    return dumper.represent_scalar('!FaceCard',
    "{0.rank!s}{0.suit!s}".format(card) )

yaml.add_representer(Card, card_representer)
yaml.add_representer(AceCard, acecard_representer)
yaml.add_representer(FaceCard, facecard_representer)

def card_constructor(loader, node):
    value = loader.construct_scalar(node)
    rank, suit= value[:-1], value[-1]
    return Card( rank, suit )

def acecard_constructor(loader, node):
    value = loader.construct_scalar(node)
    rank, suit= value[:-1], value[-1]
    return AceCard( rank, suit )

def facecard_constructor(loader, node):
    value = loader.construct_scalar(node)
    rank, suit= value[:-1], value[-1]
    return FaceCard( rank, suit )

yaml.add_constructor('!Card', card_constructor)
yaml.add_constructor('!AceCard', acecard_constructor)
yaml.add_constructor('!FaceCard', facecard_constructor)

if __name__=="__main__":
    text= yaml.dump( deck, allow_unicode=True )
    print( text )
    copy= yaml.load( text )
    print( *map(str,copy) )

# Example 3: Safe Cards
# #######################

class Card2( yaml.YAMLObject ):
    yaml_tag = '!Card2'
    yaml_loader= yaml.SafeLoader
    def __init__( self, rank, suit, hard=None, soft=None ):
        self.rank= rank
        self.suit= suit
        self.hard= hard or int(rank)
        self.soft= soft or int(rank)
    def __str__( self ):
        return "{0.rank!s}{0.suit!s}".format(self)

class AceCard2( Card2 ):
    yaml_tag = '!AceCard2'
    def __init__( self, rank, suit ):
        super().__init__( rank, suit, 1, 11 )

class FaceCard2( Card2 ):
    yaml_tag = '!FaceCard2'
    def __init__( self, rank, suit ):
        super().__init__( rank, suit, 10, 10 )

deck2 = [ AceCard2('A','♣'), Card2('2','♥'), FaceCard2('K','♦') ]

if __name__=="__main__":
    text2= yaml.dump( deck2 )
    print( "TEXT2" )
    print( text2 )
    yaml.safe_load(text2)

# Pickle
# ===================

# Example 1: Working
# ####################

# Use pickle to persist our microblog
# ::

import pickle
with open("p2_c09_travel_blog.p","wb") as target:
    pickle.dump( travel, target )

with open("p2_c09_travel_blog.p","rb") as source:
    copy= pickle.load( source )

if __name__=="__main__":
    print( copy )

# Example 2: Won't Init
# ########################

import logging,sys

audit_log= logging.getLogger( "audit" )
if __name__=="__main__":
    logging.basicConfig(stream=sys.stderr, level=logging.INFO)
else:
    logging.basicConfig(stream=sys.stderr, level=logging.ERROR)


class Hand_x:
    def __init__( self, dealer_card, *cards ):
        self.dealer_card= dealer_card
        self.cards= list(cards)
        for c in self.cards:
            audit_log.info( "Initial %s", c )
    def append( self, card ):
        self.cards.append( card )
        audit_log.info( "Hit %s", card )
    def __str__( self ):
        cards= ", ".join( map(str,self.cards) )
        return "{self.dealer_card} | {cards}".format( self=self, cards=cards )

if __name__=="__main__":
    h = Hand_x( FaceCard('K','♦'), AceCard('A','♣'), Card('9','♥') )
    print( h )

    b = pickle.dumps( h )
    h2 = pickle.loads( b )
    print( h2 )

class Hand2:
    def __init__( self, dealer_card, *cards ):
        self.dealer_card= dealer_card
        self.cards= list(cards)
        for c in self.cards:
            audit_log.info( "Initial %s", c )
    def append( self, card ):
        self.cards.append( card )
        audit_log.info( "Hit %s", card )
    def __str__( self ):
        cards= ", ".join( map(str,self.cards) )
        return "{self.dealer_card} | {cards}".format( self=self, cards=cards )
    def __getstate__( self ):
        return self.__dict__
    def __setstate__( self, state ):
        self.__dict__.update(state)
        for c in self.cards:
            audit_log.info( "Initial (unpickle) %s", c )

hp = Hand2( FaceCard('K','♦'), AceCard('A','♣'), Card('9','♥') )

data = pickle.dumps( hp )
h2p = pickle.loads( data )

# Example 3: Secure Pickle
# ########################

import builtins
class RestrictedUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if module == "builtins":
            if name not in ("exec", "eval"):
                 return getattr(builtins, name)
        elif module == "__main__":
            return globals()[name]
        # elif module in any of our application modules...
        raise pickle.UnpicklingError(
        "global '{module}.{name}' is forbidden".format(module=module, name=name))

if __name__=="__main__":
    import io
    try:
        h2s = RestrictedUnpickler(io.BytesIO(data)).load()
    except pickle.UnpicklingError as e:
        print( e )

# CSV
# ===================

# Example 1: GameStats
# ######################

# Our Simulation class definitions
# ::

class Player_Strategy_1:
    pass

class Betting:
    def __init__( self, stake=100 ):
        self.stake= stake
    def bet(self, table, game_state):
        table.bet(game_state, 1)
    def win(self, amount):
        self.stake += amount
    def loss(self, amount):
        self.stake -= amount

class Flat_Bet( Betting ):
    pass

class Martingale_Bet( Betting ):
    def __init__( self, *args ):
        self.stage = 1
        super().__init__( *args )
    def bet(self, table, game_state):
        try:
            table.bet(game_state, min(self.stage, self.stake))
        except BadBet as e:
            limit= e.args[0]
            table.bet(game_state, min(limit, self.stake))
    def win(self, amount):
        self.stage= 1
        super().win(amount)
    def loss(self, amount):
        if self.stage <= 500:
            self.stage *= 2
        super().loss(amount)

import random

class BadBet( Exception ):
    pass

class Broke( Exception ):
    pass

# A Fake simulator
# ::

class Blackjack:
    def __init__( self, play, betting ):
        self.player= play
        self.betting= betting
        self.bets= dict()
        self.rounds= 0
    @property
    def stake( self ):
        return self.betting.stake
    def bet( self, game_state, amount ):
        if amount > 50:
            raise BadBet( 50 )
        self.bets[game_state]= amount
    def play_1( self ):
        if self.betting.stake == 0:
            raise Broke
        self.betting.bet( self, 'initial' )
        bet= sum( self.bets.values() )
        if random.random() <= .45:
            if random.random() <= 1/13*4/13:
                self.betting.win(2*bet)
            else:
                self.betting.win(bet)
        else:
            self.betting.loss(bet)
    def until_broke_or_rounds( self, limit ):
        while self.rounds < limit and self.betting.stake > 0:
            self.play_1()
            self.rounds += 1

# Example 1 dumping
# ####################

# An application of the above definitions.
# ::

from collections import namedtuple
GameStat = namedtuple( "GameStat", "player,bet,rounds,final" )

def gamestat_iter( player, betting, limit=100 ):
    for sample in range(30):
        b = Blackjack( player(), betting() )
        b.until_broke_or_rounds(limit)
        yield GameStat( player.__name__, betting.__name__, b.rounds, b.betting.stake )

import csv

with open("p2_c09_blackjack.csv","w",newline="") as target:
    writer= csv.DictWriter( target, GameStat._fields )
    writer.writeheader()
    for gamestat in gamestat_iter( Player_Strategy_1, Martingale_Bet ):
        writer.writerow( gamestat._asdict() )

data = gamestat_iter( Player_Strategy_1, Martingale_Bet )
with open("p2_c09_blackjack.csv","w",newline="") as target:
    writer= csv.DictWriter( target, GameStat._fields )
    writer.writeheader()
    writer.writerows( g._asdict() for g in data )

# Example 2 loading
# ###################

# Loading data from a simulator
# ::

with open("p2_c09_blackjack.csv","r",newline="") as source:
    reader= csv.DictReader( source )
    assert set(reader.fieldnames) == set(GameStat._fields)
    for gs in ( GameStat(**r) for r in reader ):
        pass # print( gs )

def gamestat_rdr_iter(iterator):
    for row in iterator:
        yield GameStat( row['player'], row['bet'], int(row['rounds']), int(row['final']) )

if __name__=="__main__":
    with open("p2_c09_blackjack.csv","r",newline="") as source:
        reader= csv.DictReader( source )
        assert set(reader.fieldnames) == set(GameStat._fields)
        for gs in gamestat_rdr_iter(reader):
            print( gs )

# Example 3 blog and post one file
# ################################

# Our blog data to be saved positionally.
# ::

blogs = [ travel ]

with open("p2_c09_blog3.csv","w",newline="") as target:
    wtr= csv.writer( target )
    wtr.writerow(['__class__','title','date','title','rst_text','tags'])
    for b in blogs:
        wtr.writerow(['Blog',b.title,None,None,None,None])
        for p in b.entries:
            wtr.writerow(['Post',None,p.date,p.title,p.rst_text,p.tags])

# Super-important: column order must match __init__() param order.
# ::

with open("p2_c09_blog3.csv","r",newline="") as source:
    rdr= csv.reader( source )
    header= next(rdr)
    assert header == ['__class__','title','date','title','rst_text','tags']
    blogs = []
    for r in rdr:
        if r[0] == 'Blog':
            blog= Blog( *r[1:2] )
            blogs.append( blog )
        if r[0] == 'Post':
            post= Post( *r[2:] )
            blogs[-1].append( post )

# Tags, however, will not be a proper tuple
# The above doesn't handle Post tags properly!

# Must use the following
# ::

import ast
def post_builder( row ):
    return Post(
        date=datetime.datetime.strptime(row[2],"%Y-%m-%d %H:%M:%S"),
        title=row[3],
        rst_text=row[4],
        tags=ast.literal_eval(row[5]) )

with open("p2_c09_blog3.csv","r",newline="") as source:
    rdr= csv.reader( source )
    header= next(rdr)
    assert header == ['__class__','title','date','title','rst_text','tags']
    blogs = []
    for r in rdr:
        if r[0] == 'Blog':
            blog= Blog( *r[1:2] )
            blogs.append( blog )
        if r[0] == 'Post':
            post= post_builder( r )
            blogs[-1].append( post )

# Example 4 blog and post with better metadata and filter
# ########################################################

# Loading the blog with a generator function.
# ::

def blog_iter(source):
    rdr= csv.reader( source )
    header= next(rdr)
    assert header == ['__class__','title','date','title','rst_text','tags']
    blog= None
    for r in rdr:
        if r[0] == 'Blog':
            if blog:
                yield blog
            blog= Blog( *r[1:2] )
        if r[0] == 'Post':
            post= post_builder( r )
            blog.append( post )
    if blog:
        yield blog

if __name__=="__main__":
    with open("p2_c09_blog3.csv","r",newline="") as source:
        for b in blog_iter(source):
            print(b.title,[p.title for p in b.entries])

with open("p2_c09_blog3.csv","r",newline="") as source:
    blogs= list(blog_iter(source))


# Example 5 Blog and Post join
# ################################

# Using a "join" between Blog and Post to create a file.
# ::

with open("p2_c09_blog5.csv","w",newline="") as target:
    wtr= csv.writer( target )
    wtr.writerow(['Blog.title','Post.date','Post.title', 'Post.tags','Post.rst_text'])
    for b in blogs:
        for p in b.entries:
            wtr.writerow([b.title,p.date,p.title,p.tags,p.rst_text])

# Decoding column names when reconstructing the file.
# Seductive but wrong.
# ::

def make_obj( row, class_=Post ):
    prefix= class_.__name__
    column_split = ( (k,)+tuple(k.split('.')) for k in row )
    kw_args = dict( (attr,row[key])
        for key,classname,attr in column_split if classname==prefix )
    return class_( **kw_args )

import ast
def post_builder5( row ):
    return Post(
        date=datetime.datetime.strptime(
            row['Post.date'],"%Y-%m-%d %H:%M:%S"),
        title=row['Post.title'],
        rst_text=row['Post.rst_text'],
        tags=ast.literal_eval(row['Post.tags']) )


# An iterator which fetches blogs
# ::

def blog_iter2( source ):

    rdr= csv.DictReader( source )
    assert set(rdr.fieldnames) == set(['Blog.title','Post.date','Post.title', 'Post.tags','Post.rst_text'])
    row= next(rdr)
    blog= Blog(row['Blog.title'])
    post= post_builder5( row )
    blog.append( post )

    print( "Wrong:", make_obj(row,Post).as_dict() )

    for row in rdr:
        if row['Blog.title'] != blog.title:
            yield blog
            blog= Blog( row['Blog.title'] )
        post= post_builder5( row )
        blog.append( post )
    yield blog

if __name__=="__main__":
    with open("p2_c09_blog5.csv","r",newline="") as source:
        for b in blog_iter2( source ):
            print(b.title, b.as_dict())

# Legacy Files
# ===================

# We'll look at pure text and mixed text w/ packed decimal.

# Example 1 dumping all text
# ###########################

# Metadata for Gamestat objects.
# attribute name, start, size, and an output format specification.
# ::

import types

metadata_txt= types.SimpleNamespace(
    fields = [
        ('player', 0, 20, '{:<{size}s}'),
        ('bet', 20, 20, '{:<{size}s}'),
        ('rounds', 40, 5, '{:>{size}d}'),
        ('final', 45, 8, '{:>{size}d}'),
    ],
    reclen= 53,
)

# A function to transform a namedtuple into a fixed-layout record.
# ::

def gamestat_record( gamestat, metadata ):
    record= [
        format_spec.format( getattr(gamestat,name),
                size=size, )
            for name, start, size, format_spec in metadata.fields ]
    text= "".join(record)
    assert len(text) == metadata.reclen, "Got {0} != Should Be {1}".format(len(text), metadata.reclen)
    return text

# An application of the game statistics definitions.
# ::

with open("p2_c09_blackjack.file","w",encoding='cp037',newline="") as target:
    for gamestat in gamestat_iter( Player_Strategy_1, Martingale_Bet ):
        record= gamestat_record(gamestat, metadata_txt)
        target.write( record )

# Example 2 loading all text
# ##########################

# Loading data from the simulator. Part 1 -- Physical decomposition into rows.
# ::

def line_iter( aFile, metadata ):
    recBytes= aFile.read(metadata.reclen)
    while recBytes:
        yield recBytes
        recBytes= aFile.read(metadata.reclen)

# Part 2 -- decomposition into named fields.
# ::

def record_iter( aFile, metadata ):
    for line in line_iter( aFile, metadata):
        record = dict(
            (name, line[start:start+size].strip())
            for name, start, size, format_spec in metadata.fields )
        yield record

# Part 3 -- using the field to dictionary parser.
# ::

with open("p2_c09_blackjack.file","r",encoding='cp037',newline="") as source:
    for record in record_iter(source, metadata_txt):
        print(record)

# Example 3 -- USAGE DISPLAY and USAGE COMP3
# ###########################################

# Using COMP-3 expands the problem into three kinds of data
#
# - Alpha and Alphanumeric encoded in EBCDIC or ASCII
#
# - Numeric, USAGE DISPLAY, as a string of digits encoded in EBCDIC or ASCII
#
# - Numeric, USAGE COMP-3, as string of bytes encoded as packed decimal.
#
# All of which require the decimal module's Decimal class definition.

from decimal import Decimal

# As a convenience, we map 'ebcdic' to 'cp037' by adding a new lookup function.
#
# ::

import codecs
def ebcdic_lookup( name, fallback=codecs.lookup ):
    if name == 'ebcdic':
        return codecs.lookup( 'cp037' )
    return fallback( name )

codecs.register( ebcdic_lookup )

# Alphanumeric USAGE DISPLAY conversion.
# The COBOL program stored text.
# ::

def alpha_decode( data, metadata, field_metadata ):
    """Decode alpha or alphanumeric data.
    metadata has encoding.
    field_metadata is not used.

    >>> import types
    >>> meta= types.SimpleNamespace( encoding='ebcdic' )
    >>> meta.decode= codecs.getdecoder( meta.encoding )
    >>> field_meta = types.SimpleNamespace() # Not used
    >>> data = bytes( [0xf9, 0xf8, 0xf7, 0xf6, 0xf5, 0x60] )
    >>> alpha_decode( data, meta, field_meta )
    '98765-'

    """
    text, _= metadata.decode( data )
    return text

# Numeric USAGE DISPLAY trailing sign conversion.
# The COBOL program stored text version of the number.
# ::

def display_decode( data, metadata, field_metadata ):
    """Decode USAGE DISPLAY numeric data.
    metadata has encoding.
    field_metadata has attributes name, start, size, format, precision, usage.

    >>> import types
    >>> meta= types.SimpleNamespace( encoding='ebcdic' )
    >>> meta.decode= codecs.getdecoder( meta.encoding )
    >>> field_meta = types.SimpleNamespace( precision=2 )
    >>> data = bytes( [0xf9, 0xf8, 0xf7, 0xf6, 0xf5, 0x60] )
    >>> display_decode( data, meta, field_meta )
    Decimal('-987.65')

    """
    text, _= metadata.decode( data )
    precision= field_metadata.precision
    text, sign = text[:-1], text[-1]
    return Decimal(sign + text[:-precision] + '.' + text[-precision:])


# Numeric USAGE COMP-3 conversion.
# The COBOL program encoded the number into packed decimal representation.
# ::

def comp3_decode( data, metadata, field_metadata ):
    """Decode USAGE COMP-3 data.
    metadata has encoding, which is not used.
    field_metadata has attributes name, start, size, format, precision, usage.

    Note that the size is the overall resulting string of bytes.
    NOT the number of digits involved.

    >>> import types
    >>> meta= types.SimpleNamespace() # Not used
    >>> field_meta = types.SimpleNamespace( precision=2 )
    >>> data = bytes( (0x98, 0x76, 0x5d) )
    >>> comp3_decode( data, meta, field_meta )
    Decimal('-987.65')

    """
    precision= field_metadata.precision
    text= [ ]
    for b in data[:-1]:
        hi, lo = divmod( b, 16 )
        text.append( str(hi) )
        text.append( str(lo) )
    digit, sign_byte = divmod( data[-1], 16 )
    text.append( str(digit) )
    text= "".join(text)
    sign= '-' if sign_byte in (0x0b, 0x0d) else '+'
    return Decimal(sign + text[:-precision] + '.' + text[-precision:])

# Encoder for simple alpha or alphanumeric.
# ::

def alpha_encode( data, metadata, field_metadata ):
    """Encode alpha or alphanumeric data.
    metadata has encoding.
    field_metadata is not used.

    >>> import types
    >>> meta= types.SimpleNamespace( encoding='ebcdic' )
    >>> meta.encode= codecs.getencoder( meta.encoding )
    >>> field_meta = types.SimpleNamespace( size=6 )
    >>> data = '98765-'
    >>> expected= bytes( [0xf9, 0xf8, 0xf7, 0xf6, 0xf5, 0x60] )
    >>> actual= alpha_encode( data, meta, field_meta )
    >>> repr(actual)
    "b'\\\\xf9\\\\xf8\\\\xf7\\\\xf6\\\\xf5`'"
    >>> actual == expected
    True

    """
    bytes, _= metadata.encode(
        "{:<{size}s}".format(data, size=field_metadata.size) )
    return bytes

# Encoder for numeric USAGE DISPLAY, trailing sign.
# ::

def display_encode( data, metadata, field_metadata ):
    """Encode numeric USAGE DISPLAY trailing sign.
    metadata has encoding.
    field_metadata has attributes name, start, size, format, precision, usage.

    >>> import types, decimal
    >>> meta= types.SimpleNamespace( encoding='ebcdic' )
    >>> meta.encode= codecs.getencoder( meta.encoding )
    >>> field_meta = types.SimpleNamespace( size=6, precision=2 )
    >>> expected= bytes( [0xf9, 0xf8, 0xf7, 0xf6, 0xf5, 0x60] )
    >>> actual= display_encode( Decimal('-987.65'), meta, field_meta )
    >>> repr(actual)
    "b'\\\\xf9\\\\xf8\\\\xf7\\\\xf6\\\\xf5`'"
    >>> actual == expected
    True

    """
    text= "{0:0>{size}d}{1}".format(
        abs(int(data*Decimal(10)**field_metadata.precision)),
        '-' if data < 0 else '+',
        size=field_metadata.size-1 )
    bytes, _= metadata.encode( text )
    return bytes

# Encoder for numeric USAGE COMP-3.
# ::

def comp3_encode( data, metadata, field_metadata ):
    """Encode numeric USAGE COMP-3.
    metadata has encoding which is not used.
    field_metadata has attributes name, start, size, format, precision, usage.

    Note that the size is the overall resulting string of bytes.
    NOT the number of digits involved.
    This has 2 digits per byte + a digit and a sign.

    >>> import types
    >>> meta= types.SimpleNamespace( encoding='ebcdic' )
    >>> field_meta = types.SimpleNamespace( size=3, precision=2 )
    >>> expected= bytes( (0x98, 0x76, 0x5d) )
    >>> actual= comp3_encode( Decimal('-987.65'), meta, field_meta )
    >>> repr(actual)
    "b'\\\\x98v]'"
    >>> actual == expected
    True

    """
    value= abs(int(data*Decimal(10)**field_metadata.precision))
    digits = [ 0x0d if data < 0 else 0x00 ] # Trailing sign.
    nDigits= field_metadata.size*2-1
    for i in range(nDigits):
        digits = [value%10]+digits
        value //= 10
    b = bytes( (hi*16+lo for hi, lo in list(zip(digits[::2],digits[1::2]))) )
    return b


# Our expanded metadata to include more refined field-level definitions.
# First, we'll define some encode-decode pairs.
# ::

alphanumeric = ( alpha_encode, alpha_decode )
usage_display = ( display_encode, display_decode )
usage_comp3 = ( comp3_encode, comp3_decode )

# Then we'll define a more sophisticated metadata that includes the
# precision and a reference to the relevant encode-decode pair.
#
# The overall metadata encoding name is transformed into an
# encode and decode function to save lookups on a field-by-field basis.
# ::

import collections
Field= collections.namedtuple( "Field",
    "name, start, size, precision, usage" )
NS= types.SimpleNamespace
metadata_comp3= NS(
    fields = [
        Field('player', 0, 20, None, alphanumeric),
        Field('bet', 20, 20, None, alphanumeric),
        Field('rounds', 40, 8, 2, usage_display),
        Field('final', 48, 8, 2, usage_comp3),
    ],
    reclen= 56,
    encoding= 'ebcdic', # for display fields and alphanumeric fields.
)
metadata_comp3.decode= codecs.getdecoder( metadata_comp3.encoding )
metadata_comp3.encode= codecs.getencoder( metadata_comp3.encoding )

# A function to transform a namedtuple into a fixed-layout record.
# ::

def gamestat_record_comp3( gamestat, metadata ):
    record= [
        field.usage[0](getattr(gamestat,field.name),metadata,field)
        for field in metadata.fields ]
    text= b"".join(record)
    assert len(text) == metadata.reclen, "Got {0} != Should Be {1}".format(len(text), metadata.reclen)
    return text

# Example encoding app.
# ::

with open("p2_c09_blackjack_comp3.file","wb") as target:
    for gamestat in gamestat_iter( Player_Strategy_1, Martingale_Bet ):
        record= gamestat_record_comp3(gamestat, metadata_comp3)
        target.write( record )

# Example decoding iterator using more sophisticated metadata.
# ::

def record2_iter( aFile, metadata ):
    for line in line_iter( aFile, metadata):
        field_data = ( (field, line[field.start:field.start+field.size])
            for field in metadata.fields )
        record = dict(
            (field.name, field.usage[1](data, metadata, field))
            for field, data in field_data )
        yield record

with open("p2_c09_blackjack_comp3.file","rb") as source:
    for record in record2_iter( source, metadata_comp3 ):
        print( record )

# XML
# ===================

# Example 1: XML output
# ######################

class Blog_X( Blog ):
    def xml( self ):
        children= "\n".join( c.xml() for c in self.entries )
        return """\
<blog><title>{0.title}</title>
<entries>
{1}
<entries></blog>""".format(self,children)

class Post_X( Post ):
    def xml( self ):
        tags= "".join( "<tag>{0}</tag>".format(t) for t in self.tags )
        return """\
<entry>
    <title>{0.title}</title>
    <date>{0.date}</date>
    <tags>{1}</tags>
    <text>{0.rst_text}</text>
</entry>""".format(self,tags)

travel4 = Blog_X( "Travel" )
travel4.append(
    Post_X( date=datetime.datetime(2013,11,14,17,25),
        title="Hard Aground",
        rst_text="""Some embarrassing revelation. Including ☹ and ⚓""",
        tags=("#RedRanger", "#Whitby42", "#ICW"),
        )
)
travel4.append(
    Post_X( date=datetime.datetime(2013,11,18,15,30),
        title="Anchor Follies",
        rst_text="""Some witty epigram.""",
        tags=("#RedRanger", "#Whitby42", "#Mistakes"),
        )
)

if __name__=="__main__":
    print( travel4.xml() )

# Example 1: element Tree output
# ##############################

import xml.etree.ElementTree as XML

class Blog_E( Blog ):
    def xml( self ):
        blog= XML.Element( "blog" )
        title= XML.SubElement( blog, "title" )
        title.text= self.title
        title.tail= "\n"
        entities= XML.SubElement( blog, "entries" )
        entities.extend( c.xml() for c in self.entries )
        blog.tail= "\n"
        return blog

class Post_E( Post ):
    def xml( self ):
        post= XML.Element( "entry" )
        title= XML.SubElement( post, "title" )
        title.text= self.title
        date= XML.SubElement( post, "date" )
        date.text= str(self.date)
        tags= XML.SubElement( post, "tags" )
        for t in self.tags:
            tag= XML.SubElement( tags, "tag" )
            tag.text= t
        text= XML.SubElement( post, "rst_text" )
        text.text= self.rst_text
        post.tail= "\n"
        return post

travel5 = Blog_E( "Travel" )
travel5.append(
    Post_E( date=datetime.datetime(2013,11,14,17,25),
        title="Hard Aground",
        rst_text="""Some embarrassing revelation. Including ☹ and ⚓""",
        tags=("#RedRanger", "#Whitby42", "#ICW"),
        )
)
travel5.append(
    Post_E( date=datetime.datetime(2013,11,18,15,30),
        title="Anchor Follies",
        rst_text="""Some witty epigram. Including < & > characters.""",
        tags=("#RedRanger", "#Whitby42", "#Mistakes"),
        )
)

if __name__=="__main__":
    tree= XML.ElementTree( travel5.xml() )
    text= XML.tostring(tree.getroot())
    print( text )

import ast
if __name__=="__main__":
    doc= XML.parse( io.StringIO(text.decode('utf-8')) )
    xml_blog= doc.getroot()
    blog= Blog( xml_blog.findtext('title') )
    for xml_post in xml_blog.findall('entries/entry'):
        tags= [t.text for t in xml_post.findall( 'tags/tag' )]
        post= Post(
            date= datetime.datetime.strptime(
                xml_post.findtext('date'), "%Y-%m-%d %H:%M:%S"),
            title=xml_post.findtext('title'),
            tags=tags,
            rst_text= xml_post.findtext('rst_text')
         )
        blog.append( post )
    render( blog )
