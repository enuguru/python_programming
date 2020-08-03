#!/usr/bin/env python3

# Enriching immutable objects
# ----------------------------


# Gather some basic timing information on transformation.
# In this case, it's "enrichment" where we're adding derived
# values.
#
# Compare wrapping, rebuilding and replacing.
#
# We need to work with a consistent piece of information.
# In this case, it's a CSV extract of a logfile.
#
# Here are the first two lines of the file.
#
# parsed-literal::
#
#   host,identity,user,time,request,status,bytes,referer,user_agent
#   67.141.136.237,-,-,31/Jan/2012:22:10:56 -0500,GET /homepage/books/nonprog/html/p13_modules/p13_c04_time.html HTTP/1.1,200,105147,http://www.google.com/url?sa=t&rct=j&q=datetime%20module%20history%20python&source=web&cd=12&ved=0CC8QFjABOAo&url=http%3A%2F%2Fwww.itmaybeahack.com%2Fhomepage%2Fbooks%2Fnonprog%2Fhtml%2Fp13_modules%2Fp13_c04_time.html&ei=Np4oT-i_O6qs2gXMiPHDAg&usg=AFQjCNFB4RlXe3fbdR4T2FiR7-vcM7kx4A,Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2.24) Gecko/20111103 Firefox/3.6.24 ( .NET CLR 3.5.30729; .NET4.0C)

#
# We'll parse this with the csv module, creating named tuples

import csv
from collections import namedtuple
Access = namedtuple('Access',
    ['host', 'identity', 'user', 'time', 'request',
    'status', 'bytes', 'referer', 'user_agent'] )

# Here's an example iterator which simply reads the file.
# ::

with open("cache_d.csv") as source:
    rdr= csv.reader(source)
    next(rdr) # Skip the header
    access_iter= ( Access(*row) for row in rdr )
    for a in access_iter:
        pass

# Here's an iterator which does a "simple" date-time conversion.
# ::
import datetime
def parse_time( ts ):
    return datetime.datetime.strptime( ts, "%d/%b/%Y:%H:%M:%S %z" )

# Here's an enrichment which wraps using a sequential CSV reader.
# ::

TimeAccess1 = namedtuple('TimeAccess1', ['datetime','access'] )

def enrich_wrap_seq( source ):
    rdr= csv.reader(source)
    next(rdr) # Skip the header
    access_iter= ( Access(*row) for row in rdr )
    for a in access_iter:
        yield TimeAccess1(parse_time(a.time), a)

# Here's a variant which wraps by uses a dictionary CSV reader.
# ::

def enrich_wrap_dict( source ):
    rdr= csv.DictReader(source)
    access_iter= ( Access(**row) for row in rdr )
    for a in access_iter:
        yield TimeAccess1(parse_time(a.time), a)

# Here's an enrichment which rebuilds a new, flat tuple
# ::

TimeAccess2 = namedtuple('TimeAccess2',
    ('datetime',) + Access._fields )

def enrich_rebuild( source ):
    rdr= csv.reader(source)
    next(rdr) # Skip the header
    access_iter= ( Access(*row) for row in rdr )
    for a in access_iter:
        yield TimeAccess2(parse_time(a.time), *a)

# Here's an enrichment which replaces a field in an existing tuple.
# Really, we're building a new tuple.
# ::

TimeAccess3 = namedtuple('Access',
    ['datetime', 'host', 'identity', 'user', 'time', 'request',
    'status', 'bytes', 'referer', 'user_agent'] )

def enrich_replace( source ):
    rdr= csv.reader(source)
    next(rdr) # Skip the header
    access_iter= ( TimeAccess3(None, *row) for row in rdr )
    for a in access_iter:
        yield a._replace( datetime= parse_time(a.time) )

# Here's the classical stateful object enrichment.

class TimeAccess4:
    def __init__( self, *args ):
        self.__dict__.update( zip(
            ['host', 'identity', 'user', 'time', 'request',
            'status', 'bytes', 'referer', 'user_agent'], args ) )

def enrich_update( source ):
    rdr= csv.reader(source)
    next(rdr) # Skip the header
    access_iter= ( TimeAccess4(*row) for row in rdr )
    for a in access_iter:
        a.datetime= parse_time(a.time)
        yield a

# Here's an overall process that wants enriched objects.
# ::

def process( enrichment_iter ):
    with open("cache_d.csv") as source:
        for row in enrichment_iter( source ):
            pass

# Some timeit setup
# ::

import timeit
fmt= "{0:16s} {1:5.2f}"
def report( label, function, args ):
    start= timeit.default_timer()
    function( *args )
    end= timeit.default_timer()
    print( fmt.format( label, end-start ) )

report( "Wrap (Seq)", process, (enrich_wrap_seq,) )

report( "Wrap (Dict)", process, (enrich_wrap_dict,) )

report( "Rebuild", process, (enrich_rebuild,) )

report( "Replace", process, (enrich_replace,) )

report( "Update", process, (enrich_update,) )

