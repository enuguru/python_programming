Python textmining package
=========================

Author: Christian Peccei
Author Email: cpeccei@hotmail.com
Version: 1.0
Homepage: http://www.christianpeccei.com/projects/textmining

Overview
--------

This package contains a variety of useful functions for text mining in Python.
It focuses on statistical text mining (i.e. the bag-of-words model) and makes it
very easy to create a term-document matrix from a collection of documents. This
matrix can then be read into a statistical package (R, MATLAB, etc.) for further
analysis. The package also provides some useful utilities for finding
collocations (i.e. significant two-word phrases), computing the edit distance
between words, and chunking long documents up into smaller pieces.

The package has a large amount of curated data (stopwords, common names, an
English dictionary with parts of speech and word frequencies) which allows the
user to extract fairly sophisticated features from a document.

This package does NOT have any natural language processing capabilities such as
part-of-speech tagging. Please see the Python NLTK for that sort of
functionality (plus much, much more).

Installation
------------

Extract the .zip file and run:

python setup.py install

Documentation
-------------

Please see the docstrings in the functions themselves and the 'examples'
subdirectory for actual applications of the various functions.
