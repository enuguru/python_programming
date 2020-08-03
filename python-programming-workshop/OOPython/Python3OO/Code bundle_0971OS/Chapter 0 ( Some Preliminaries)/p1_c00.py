#!/usr/bin/env python3.3

# Chapter 0 -- Some Preliminaries
# -----------------------------------

# In order to run the examples mentioned in this book you require the following software: 

# Python version 3.2 or higher with the standard suite of libraries. We'll focus on Python 3.3, but the differences from 3.2 are minor.

# We'll look at some additional packages. These include PyYaml, SQLAlchemy, and Jinja2.

# http://pyyaml.org

# http://www.sqlalchemy.org When building this, check the installation guide, http://docs.sqlalchemy.org/en/rel_0_9/intro.html#installation. Using the --without-cextensions option can simplify installation.

# http://jinja.pocoo.org/

# Optionally, you may want to add Sphinx or Docutils to your environment, as we'll touch on them, also.

# http://sphinx-doc.org

# http://docutils.sourceforge.net

# The step-by-step setup will very somewhat, but it will be something like the following:
#
# 1.	Install Python 3.3 from http://www.python.org.
#
# 2.	Install setuptools from https://pypi.python.org/pypi/setuptools/2.2. 
#
#		On some systems, this will install everything you need. For Mac OS X, however,
#		the default Python will be the OS 2.7 version. 
# 
#		See https://pypi.python.org/pypi/setuptools/2.2#unix-based-systems-including-mac-os-x 
#		for instructions suitable for Mac OS installation.
#
#   	::
#
#       	wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | sudo python3.3
#
#
# 3.	Use easy_install-3.3 to install the other packages: 
#
#		-  ``sudo easy_install-3.3 pyyaml``
#
#		-  ``sudo easy_install-3.3 sqlalchemy``
#
#		-  ``sudo easy_install-3.3 jinja2``
#
#		-  ``sudo easy_install-3.3 sphinx``
#
#		-  ``sudo easy_install-3.3 docutils``
# 
# ..  sectnum::
#
# ..  contents::
#

# Timeit
# ==============================

# Two quick examples to show the basics of timeit.
# ::

import timeit
timeit.timeit( "obj.method()", """
class SomeClass:
    def method(self):
        pass
obj= SomeClass()
""")

timeit.timeit( "f()","""
def f():
    pass
""" )

# Unit Test
# ==============================

# Definition of a simple class hierarchy that defines some unit tests.
# ::

import types
import unittest

class EmptyClass:
    pass

# Generic superclass for tests.
# ::

class TestAccess( unittest.TestCase ):
    def test_should_add_and_get_attribute( self ):
        self.object.new_attribute= True
        self.assertTrue( self.object.new_attribute )
    def test_should_fail_on_missing( self ):
        self.assertRaises( AttributeError, lambda: self.object.undefined )

# Concrete subclasses
# ::

class Test_EmptyClass( TestAccess ):
    def setUp( self ):
       self.object= EmptyClass()

class Test_Namespace( TestAccess ):
    def setUp( self ):
       self.object= types.SimpleNamespace()

class Test_Object( TestAccess ):
    def setUp( self ):
       self.object= object()

# Tests show that ``object`` doesn't work like SimpleNamespace or EmptyClass.

# A unit test suite. While not required, it's recommended as a way to
# assemble large groups of tests for large applications.
# ::

def suite():
    s= unittest.TestSuite()
    s.addTests( unittest.defaultTestLoader.loadTestsFromTestCase(Test_EmptyClass) )
    s.addTests( unittest.defaultTestLoader.loadTestsFromTestCase(Test_Namespace) )
    s.addTests( unittest.defaultTestLoader.loadTestsFromTestCase(Test_Object) )
    return s

# The typical main program for a test module.
# ::

if __name__ == "__main__":
    t= unittest.TextTestRunner()
    t.run( suite() )

# Docstring Example
# =============================

# Simple function with docstring.
# ::

def factorial( n ):
    """Compute n! recursively.

    :param n: an integer >= 0
    :returns: n!

    Because of Python's stack limitation, this won't
    compute a value larger than about 1000!.

    >>> factorial(5)
    120
    """
    if n == 0: return 1
    return n*factorial(n-1)

print( "5!==", factorial(5) )
