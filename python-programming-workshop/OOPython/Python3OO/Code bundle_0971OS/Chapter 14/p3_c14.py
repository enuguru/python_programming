#!/usr/bin/env python3

# Chapter 14 -- Logging and Warnings
# --------------------------------------------

# ..  sectnum::
#
# ..  contents::
#

# Simple Logging
# ========================

# Define a decorator
# ::

def logged( class_ ):
    class_.logger= logging.getLogger( class_.__qualname__ )
    return class_

# This is wedged into a function to prevent polluting other examples with
# configuration.

# ::

def demo1():

    import logging
    import sys

    # Add a level
    # ::

    logging.addLevelName( 15, "VERBOSE" )
    logging.VERBOSE= 15


    # Sample Class
    # ::

    @logged
    class Player:
        def __init__( self, bet, strategy, stake ):
            self.logger.debug( "init bet {0}, strategy {1}, stake {2}".format(
                bet, strategy, stake) )

    # No configuration -- no output
    # ::

    print( "Create Player 1" )
    p1= Player( "Bet1", "Strategey1", 1 )

    # Configuration changed -- now there's output
    # ::

    logging.basicConfig( stream=sys.stderr, level=logging.DEBUG )

    print( "Create Player 2" )
    p2= Player( "Bet2", "Strategy2", 2 )

    logging.shutdown()

# Multiple Loggers
# ===========================

# This is wedged into a function to prevent polluting other examples with
# configuration.

# ::

def demo2():

    # Expanded Decorator
    # ::

    def log_to( *names ):
        if len(names) == 0:
            names= ['logger']
        def concrete_log_to( class_ ):
            for log_name in names:
                setattr( class_, log_name, logging.getLogger(
                    log_name + "." + class_.__qualname__ ) )
            return class_
        return concrete_log_to

    # Sample Class
    # :

    @log_to( "audit", "verbose" )
    class Player:
        def __init__( self, bet, strategy, stake ):
            self.audit.info( "Initial {0:d}".format(stake) )
            self.verbose.info( "Init bet={bet:s} strategy={strategy:s} stake={stake:d}".format(
                bet=bet, strategy=strategy, stake=stake ) )

    @log_to("security")
    class Table:
        def add_player( self, player ):
            self.security.info( "Adding {0}".format(player) )

    # Demo Output
    # ::

    print( "Create Player 2" )
    p3= Player("Bet3", "Strategy3", 3)
    t= Table()
    t.add_player( p3 )

    logging.shutdown()

# Multiple Loggers with YAML Config
# =============================================

# Sample configuration file
# ::

config3="""
version: 1
handlers:
  console:
    class: logging.StreamHandler
    stream: ext://sys.stderr
    formatter: basic
  audit_file:
    class: logging.FileHandler
    filename: p3_c14_audit.log
    encoding: utf-8
    formatter: basic
formatters:
  basic:
    style: "{"
    format: "{levelname:s}:{name:s}:{message:s}"
loggers:
  verbose:
    handlers: [console]
    level: INFO
    propagate: False # Added
  audit:
    handlers: [console,audit_file]
    level: INFO
    propagate: False # Added
root: # Added
  handlers: [console]
  level: INFO
"""

def demo3():

    # Parsing
    # ::

    import logging.config
    import yaml
    config_dict= yaml.load(config3)
    print( config_dict )
    logging.config.dictConfig(config_dict)

    # Logging
    # ::

    verbose= logging.getLogger( "verbose.example.SomeClass" )
    audit= logging.getLogger( "audit.example.SomeClass" )
    verbose.info( "Verbose information" )
    audit.info( "Audit record with before and after" )

    print( "Root Handlers:", logging.getLogger().handlers )
    print( "Verbose Handlers:", logging.getLogger('verbose').handlers )
    print( "Audit Handlers:", logging.getLogger('audit').handlers )

# Startup/Shutdown
# =============================================

# Some main function
# ::

from collections import Counter
class Main:
    def __init__( self ):
        self.balance= Counter()
        self.log= logging.getLogger( self.__class__.__qualname__ )
    def run( self ):
        self.log.info( "Start" )

        # Some processing
        self.balance['count'] += 1
        self.balance['balance'] += 3.14

        self.log.info( "Counts {0}".format(self.balance) )

        for k in self.balance:
            self.log.info( "{0:.<16s} {1:n}".format(
                k, self.balance[k]) )

# Main program
# ::

def demo4a():

    import sys
    import logging
    import logging.config
    import yaml
    logging.config.dictConfig( yaml.load(config3) )
    try:
        application= Main()
        status= application.run()
    except Exception as e:
        logging.exception( e )
        status= 2
    finally:
        logging.shutdown()
    #sys.exit(status)

# Atexit
# ::

def demo4b():

    import atexit
    import logging
    import logging.config
    import yaml
    import sys
    logging.config.dictConfig( yaml.load(config3) )
    atexit.register(logging.shutdown)
    try:
        application= Main()
        status= application.run()
    except Exception as e:
        logging.exception( e )
        status= 2
    #sys.exit(status)
    
# A context manager can be used, also. See `Chapter 16 <file:p3_c16.html>`_.
# Note that there are profound limitations when using dictConfig.
# Anything loggers created prior to running dictConfig wind up disconnected.
# Be sure to include ``disable_existing_loggers: False`` in the dictionary.


# Debugging
# ==================

# New Config
# ::

config5="""
version: 1
disable_existing_loggers: False
handlers:
  console:
    class: logging.StreamHandler
    stream: ext://sys.stderr
    formatter: basic
  audit_file:
    class: logging.FileHandler
    filename: p3_c14_audit.log
    encoding: utf-8
    formatter: detailed
formatters:
  basic:
    style: "{"
    format: "{levelname:s}:{name:s}:{message:s}"
  detailed:
    style: "{"
    format: "{levelname:s}:{name:s}:{asctime:s}:{message:s}"
    datefmt: "%Y-%m-%d %H:%M:%S"
loggers:
  audit:
    handlers: [console,audit_file]
    level: INFO
    propagate: False
root:
  handlers: [console]
  level: INFO
"""

def demo5():

    # Some classes
    # ::

    @logged
    class BettingStrategy:
        def bet( self ):
            raise NotImplementedError( "No bet method" )
        def record_win( self ):
            pass
        def record_loss( self ):
            pass

    @logged
    class OneThreeTwoSix( BettingStrategy ):
        def __init__( self ):
            self.wins= 0
        def _state( self ):
            return dict( wins= self.wins )
        def bet( self ):
            bet= { 0: 1, 1: 3, 2: 2, 3: 6 }[self.wins%4]
            self.logger.debug( "Bet {1}; based on {0}".format(self._state(), bet) )
        def record_win( self ):
            self.wins += 1
            self.logger.debug( "Win: {0}".format(self._state()) )
        def record_loss( self ):
            self.wins = 0
            self.logger.debug( "Loss: {0}".format(self._state()) )

    # A Decorator
    # ::

    def audited( class_ ):
        class_.logger= logging.getLogger( class_.__qualname__ )
        class_.audit= logging.getLogger( "audit." + class_.__qualname__ )
        return class_

    @audited
    class Table:
        def bet( self, bet, amount ):
            self.audit.info( "Bet {0} Amount {1}".format(bet, amount) )

    # A Main Program demo
    # ::

    import atexit
    logging.config.dictConfig( yaml.load(config5) )
    atexit.register(logging.shutdown)
    log= logging.getLogger( "main" )
    log.info( "Starting" )
    application= Table()
    application.bet( "One", 1 )
    application.bet( "Two", 2 )
    log.info( "Finish" )
    logging.shutdown()

# Extending
# ====================

# Doesn't seem to work as expected.

def demo_6():

    # Note that the factory is somehow bypassed by a LoggerAdapter
    # ::

    from collections.abc import Callable
    class UserLogRecord( Callable ):
        def __init__( self ):
            self.previous = logging.getLogRecordFactory()
        def __call__( self, *args, **kwargs ):
            print( "Building log with ", args, kwargs, getattr(self,'extra',{}) )
            user= kwargs.pop('user',None)
            record = self.previous(*args, **kwargs)
            record.user= user
            return record

    # Adapter. This kind of extension may not be needed.
    # The "extra" is set as the default behavior.
    # However, the processing is obscure. It behaves as if it bypassed the factory.
    # Yet. The code looks like it won't bypass the factory.
    # ::

    class UserLogAdapter( logging.LoggerAdapter ):
        def process( self, msg, kwargs ):
            kwargs['user']= self.extra.get('user',None)
            return msg, kwargs

    # Installation
    # ::

    logging.config.dictConfig( yaml.load(config5) )
    logging.setLogRecordFactory(UserLogRecord())

    # Use
    # ::

    log= logging.getLogger( "test.demo6" )
    for h in logging.getLogger().handlers:
        h.setFormatter( logging.Formatter( fmt="{user}:{name}:{levelname}:{message}", style="{") )

    import threading
    data= threading.local()
    data.user= "Some User"
    data.ip_address= "127.0.0.1"

    log.info( "message without User" )

    # auth_log= logging.LoggerAdapter( log, data.__dict__ ) # "Attempt to overwrite 'user' in LogRecord"
    # auth_log= UserLogAdapter( log, data.__dict__ ) # _log() got an unexpected keyword argument 'user'
    # auth_log.info( "message with User" )

# Warnings
# ====================

# Deprecation
# ::

import warnings
class Player:
    __version__= "2.1"
    def bet( self ):
        warnings.warn( "bet is deprecated, use place_bet", DeprecationWarning, stacklevel=2 )
        pass

warnings.simplefilter("always", category=DeprecationWarning)
p2= Player()
p2.bet()

# Configuration
# ::

import warnings
try:
    import simulation_model_1 as model
except ImportError as e:
    warnings.warn( e )
if 'model' not in globals():
    try:
        import simulation_model_2 as model
    except ImportError as e:
        warnings.warn( e )
if 'model' not in globals():
    #raise ImportError( "Missing simulation_model_1 and simulation_model_2" )
    pass

# Tail Buffer
# ========================

# Class Definion
# ::

import logging
import logging.config
import logging.handlers
import yaml

class TailHandler( logging.handlers.MemoryHandler ):
    def shouldFlush(self, record):
        """
        Check for buffer full or a record at the flushLevel or higher.
        """
        if record.levelno >= self.flushLevel: return True
        while len(self.buffer) >= self.capacity:
            self.acquire()
            try:
                del self.buffer[0]
            finally:
                self.release()

# Configuration
# ::

config8="""
version: 1
disable_existing_loggers: False
handlers:
  console:
    class: logging.StreamHandler
    stream: ext://sys.stderr
    formatter: basic
  tail:
    (): __main__.TailHandler
    target: cfg://handlers.console
    capacity: 5
formatters:
  basic:
    style: "{"
    format: "{levelname:s}:{name:s}:{message:s}"
loggers:
  test:
    handlers: [tail]
    level: DEBUG
    propagate: False
root:
  handlers: [console]
  level: INFO
"""

def demo8():

    # Installation
    # ::

    logging.config.dictConfig( yaml.load(config8) )
    log= logging.getLogger( "test.demo8" )

    # Use Case 1 -- last 5 before ERROR.

    print( "Last 5 before error" )

    for i in range(20):
        log.debug( "Message {:d}".format(i) )

    log.error( "Error causes dump of last 5" )

    # Use Case 2 -- last 5 before shutdown.
    # ::

    print( "Last 5 before shutdown" )

    for i in range(20,40):
        log.debug( "Message {:d}".format(i) )

    logging.shutdown()


# Producer/Consumer
# ==========================

# The Consumer
# ::

consumer_config = """\
version: 1
disable_existing_loggers: False
handlers:
  console:
    class: logging.StreamHandler
    stream: ext://sys.stderr
    formatter: basic
formatters:
  basic:
    style: "{"
    format: "{levelname:s}:{name:s}:{message:s}"
loggers:
  combined:
    handlers: [ console ]
    formatter: detail
    level: INFO
    propagate: False
root:
  handlers: [ console ]
  level: INFO
"""

import collections
import logging
import multiprocessing
class Log_Consumer_1(multiprocessing.Process):
    """In effect, an instance of QueueListener."""
    def __init__( self, queue ):
        self.source= queue
        super().__init__()
        logging.config.dictConfig( yaml.load(consumer_config) )
        self.combined= logging.getLogger( "combined." + self.__class__.__qualname__ )
        self.log= logging.getLogger( self.__class__.__qualname__  )
        self.counts= collections.Counter()
    def run( self ):
        self.log.info( "Consumer Started" )
        while True:
            log_record= self.source.get()
            if log_record == None: break
            self.combined.handle( log_record )
            words= log_record.getMessage().split()
            self.counts[words[0],words[1]] += 1
        self.log.info( "Consumer Finished" )
        self.log.info( self.counts )

# The Producers
# ::

class Log_Producer(multiprocessing.Process):
    handler_class= logging.handlers.QueueHandler
    def __init__( self, proc_id, queue ):
        self.proc_id= proc_id
        self.destination= queue
        super().__init__()
        self.log= logging.getLogger(
            "{0}.{1}".format(self.__class__.__qualname__, self.proc_id) )
        self.log.handlers = [ self.handler_class( self.destination ) ]
        self.log.setLevel( logging.INFO )
    def run( self ):
        self.log.info( "Producer {0} Started".format(self.proc_id) )
        for i in range(100):
            self.log.info( "Producer {:d} Message {:d}".format(self.proc_id, i) )
        self.log.info( "Producer {0} Finished".format(self.proc_id) )

def demo9():

    # The Queue
    # ::

    import multiprocessing
    queue1= multiprocessing.Queue(100) # Waaayyyy too small

    # The consumer process
    # ::

    consumer = Log_Consumer_1( queue1 )
    consumer.start()

    # The producers
    # ::

    producers = []
    for i in range(10):
        proc= Log_Producer( i, queue1 )
        proc.start()
        producers.append( proc )

    # Normal termination
    # ::

    for p in producers:
        p.join()

    queue1.put( None )

    consumer.join()

    logging.shutdown()

# Modified Queue Handler
# ==================================

# Extended QueueHandler class
# ::

class WaitQueueHandler( logging.handlers.QueueHandler ):
    def enqueue(self, record):
        self.queue.put( record )

# Revised Producer
# ::

class Log_Producer_2(Log_Producer):
    handler_class= WaitQueueHandler

# The Queue
# ::

import multiprocessing
queue2= multiprocessing.Queue(100) # Waaayyyy too small

# The consumer process
# ::

consumer2 = Log_Consumer_1( queue2 )
consumer2.start()

# The producers
# ::

producers = []
for i in range(10):
    proc= Log_Producer_2( i, queue2 )
    proc.start()
    producers.append( proc )

# Normal termination
# ::

for p in producers:
    p.join()

queue2.put( None )

consumer2.join()

logging.shutdown()
