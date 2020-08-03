import re
import stemmer
import csv
import os

data_dir = os.path.join(__path__[0], 'data')

def read_stopwords():
    """Return a set of stopwords stored in textmining.stopwords"""
    stopwords = set()
    f = open(os.path.join(data_dir, 'stopwords.txt'))
    for line in f:
        word = line.strip()
        if not word:
            continue
        stopwords.add(word)
    f.close()
    return stopwords

def read_dictionary():
    """
    Return a dict containing an English dictionary with word frequencies.
    Stored in textmining.dictionary upon initialization.

    This English dictionary was created by processing the
    unlemmatized word frequency list from the National British
    Corpus found at http://www.kilgarriff.co.uk/bnc-readme.html

    Each line contains a word followed by the relative frequency of its use
    as different parts of speech in the corpus. Please see the file
    poscodes.html in this module's doc directory for a list of the codes.
    The file is also available online at
    http://www.kilgarriff.co.uk/BNClists/poscodes.html

    """
    dictionary = {}
    f = open(os.path.join(data_dir, 'dictionary.txt'))
    for line in f:
        fields = line.split()
        word = fields[0]
        freqs = [int(x) for x in fields[1::2]]
        pos = fields[2::2]
        dictionary[word] = zip(freqs, pos)
    f.close()
    return dictionary
    
def read_names(name_file):
    """
    Read name file and return a dict containing names and frequencies.

    Three name variables are created upon initialization:
    textmining.names_male, textmining.names_female, textmining.names_last

    The name files are from the US Census Bureau at
    http://www.census.gov/genealogy/names/names_files.html

    """
    names = {}
    f = open(os.path.join(data_dir, name_file))
    for line in f:
        name, pct, cumpct, rank = line.split()
        names[name.lower()] = float(pct)
    f.close()
    return names

# Initialize useful data for text mining
names_male = read_names('names_male.txt')
names_female = read_names('names_female.txt')
names_last = read_names('names_last.txt')
dictionary = read_dictionary()
stopwords = read_stopwords()

def simple_tokenize(document):
    """
    Clean up a document and split into a list of words.

    Converts document (a string) to lowercase and strips out everything which
    is not a lowercase letter.

    """
    document = document.lower()
    document = re.sub('[^a-z]', ' ', document)
    return document.strip().split()

def simple_tokenize_remove_stopwords(document):
    """
    Clean up a document and split into a list of words, removing stopwords.

    Converts document (a string) to lowercase and strips out everything
    which is not a lowercase letter. Then removes stopwords.

    """
    document = document.lower()
    document = re.sub('[^a-z]', ' ', document)
    words = document.strip().split()
    # Remove stopwords
    words = [word for word in words if word not in stopwords]
    return words

def collapse_ngrams(words, ngrams):
    """
    Finds and collapses ngrams (i.e. multiword phrases) in a list of words.
    The ngrams should be a list of tuples. Note that the ngrams are in the
    same format returned by the bigram_collocations function. This makes it
    easy to use bigram_collocations to find significant two-word phrases in
    a corpus and then use collapse_ngrams to build a tokenizer that treats
    these phrases as single tokens.

    Note: the input words should not contain any "|" or "_" characters as
    these are used internally by the algorithm and may confuse it.

    Example:

    words = ['new', 'york', 'city', 'is', 'the', 'big', 'apple']
    ngrams = [('new', 'york', 'city'), ('big', 'apple')]
    
    collapse_ngrams(words, ngrams) then gives:
    ['new_york_city', 'is', 'the', 'big_apple']

    """
    # Check that words are free of special characters
    testwords = ''.join(words)
    if '|' in testwords or '_' in testwords:
        raise ValueError('Input words should not contain any "|" or "_"')
    # Proceed with algorithm
    wordstring = '|'.join(words)
    for ngram in ngrams:
        old = '|'.join(ngram)
        new = '_'.join(ngram)
        wordstring = wordstring.replace(old, new)
    return wordstring.split('|')

def stem(word):
    """
    Returns Porter stemmed version of words.

    Input can either be a string or list of strings.

    """
    p = stemmer.PorterStemmer()
    if isinstance(word, str):
        # Input is a single word
        return p.stem(word, 0, len(word) - 1)
    else:
        # Assume input is a list ot words
        return [p.stem(w, 0, len(w) - 1) for w in word]
        
def editdistance(a, b):
    """
    Calculates the Levenshtein distance between a and b.

    From http://hetland.org/coding/python/levenshtein.py

    """
    n, m = len(a), len(b)
    if n > m:
        # Make sure n <= m, to use O(min(n,m)) space
        a, b = b, a
        n, m = m, n
    current = range(n + 1)
    for i in range(1, m + 1):
        previous, current = current, [i] + [0] * n
        for j in range(1, n+1):
            add, delete = previous[j] + 1, current[j - 1] + 1
            change = previous[j - 1]
            if a[j - 1] != b[i - 1]:
                change = change + 1
            current[j] = min(add, delete, change)
    return current[n]

def readblocks(source,
               isnewblock=lambda x,y: x.strip() and not y.strip()):
    """
    Returns a generator for iterating over blocks of lines.

    The isnewblock function must take in two lines and return a boolean
    indicating whether there is a block separator between them. The default
    function reads by paragraph (i.e. if the first line is all spaces and
    the next contains text then it is a new block).

    """
    block = None
    for b in source:
        if block is None:
            block = [b]
            continue
        if isnewblock(block[-1], b):
            yield block
            block = []
        block.append(b)
    yield block


def paragraph_boundary(line1, line2):
    """
    Returns True if a paragraph boundary falls between line1 and line2.

    A helper function for the splitby function. Given two strings containing
    successive lines from a text document, this will return True if line1 is
    the end of a paragraph (i.e. if line1 has text and line2 is blank).

    """
    return line1.strip() and not line2.strip()

def splitby(source, split=paragraph_boundary):
    """
    Split an iterator into groups using a function to define split boundaries.

    The split function should take in two successive elements of the source
    iterator and return a boolean indicating whether there is group boundary
    between them. The default function splits by paragraph.

    """
    group = None
    for b in source:
        if group is None:
            # Add the first element of the iterator to the current group
            group = [b]
            continue
        if split(group[-1], b):
            yield group
            group = []
        group.append(b)
    yield group

def bigram_collocations(words, power=3):
    """
    Find bigram collocations in a list of words.

    Given a list of words (usually a long list, such as a novel)
    this will return a list of bigram collocations (i.e. two-word
    phrases that occur more often than would be expected by chance).
    Stronger collocations appear at the start of the list.

    This code was adapted from the collocation code in
    http://www.semanticbible.com/other/talks/2008/nltk/nltk.html

    """
    # Count frequency of each separate word
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    # Count frequency of each bigram
    bigram_count = {}
    for bigram in zip(words, words[1:]):
        bigram_count[bigram] = bigram_count.get(bigram, 0) + 1
    # Score all the bigrams by the strength of their collocation
    scored = []
    for bigram in bigram_count:
        word1, word2 = bigram
        # Ignore any bigrams involving stopwords
        if word1 in stopwords or word2 in stopwords:
            continue
        # Ignore infrequently occurring bigrams
        if bigram_count[bigram] < 3:
            continue
        freq1 = word_count[word1]
        freq2 = word_count[word2]
        freq12 = bigram_count[bigram]
        score = freq12 ** power / float(freq1 * freq2)
        scored.append((score, bigram))
    scored.sort(reverse=True)
    return [s[1] for s in scored]


class TermDocumentMatrix(object):

    """
    Class to efficiently create a term-document matrix.

    The only initialization parameter is a tokenizer function, which should
    take in a single string representing a document and return a list of
    strings representing the tokens in the document. If the tokenizer
    parameter is omitted it defaults to using textmining.simple_tokenize

    Use the add_doc method to add a document (document is a string). Use the
    write_csv method to output the current term-document matrix to a csv
    file. You can use the rows method to return the rows of the matrix if
    you wish to access the individual elements without writing directly to a
    file.

    """

    def __init__(self, tokenizer=simple_tokenize):
        """Initialize with tokenizer to split documents into words."""
        # Set tokenizer to use for tokenizing new documents
        self.tokenize = tokenizer
        # The term document matrix is a sparse matrix represented as a
        # list of dictionaries. Each dictionary contains the word
        # counts for a document.
        self.sparse = []
        # Keep track of the number of documents containing the word.
        self.doc_count = {}

    def add_doc(self, document):
        """Add document to the term-document matrix."""
        # Split document up into list of strings
        words = self.tokenize(document)
        # Count word frequencies in this document
        word_counts = {}
        for word in words:
            word_counts[word] = word_counts.get(word, 0) + 1
        # Add word counts as new row to sparse matrix
        self.sparse.append(word_counts)
        # Add to total document count for each word
        for word in word_counts:
            self.doc_count[word] = self.doc_count.get(word, 0) + 1

    def rows(self, cutoff=2):
        """Helper function that returns rows of term-document matrix."""
        # Get master list of words that meet or exceed the cutoff frequency
        words = [word for word in self.doc_count \
          if self.doc_count[word] >= cutoff]
        # Return header
        yield words
        # Loop over rows
        for row in self.sparse:
            # Get word counts for all words in master list. If a word does
            # not appear in this document it gets a count of 0.
            data = [row.get(word, 0) for word in words]
            yield data

    def write_csv(self, filename, cutoff=2):
        """
        Write term-document matrix to a CSV file.

        filename is the name of the output file (e.g. 'mymatrix.csv').
        cutoff is an integer that specifies only words which appear in
        'cutoff' or more documents should be written out as columns in
        the matrix.

        """
        f = csv.writer(open(filename, 'wb'))
        for row in self.rows(cutoff=cutoff):
            f.writerow(row)
