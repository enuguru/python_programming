import textmining
import os

def termdocumentmatrix_example():
    # Create some very short sample documents
    doc1 = 'John and Bob are brothers.'
    doc2 = 'John went to the store. The store was closed.'
    doc3 = 'Bob went to the store too.'
    # Initialize class to create term-document matrix
    tdm = textmining.TermDocumentMatrix()
    # Add the documents
    tdm.add_doc(doc1)
    tdm.add_doc(doc2)
    tdm.add_doc(doc3)
    # Write out the matrix to a csv file. Note that setting cutoff=1 means
    # that words which appear in 1 or more documents will be included in
    # the output (i.e. every word will appear in the output). The default
    # for cutoff is 2, since we usually aren't interested in words which
    # appear in a single document. For this example we want to see all
    # words however, hence cutoff=1.
    tdm.write_csv('matrix.csv', cutoff=1)
    # Instead of writing out the matrix you can also access its rows directly.
    # Let's print them to the screen.
    print '\ntermdocumentmatrix_example 1\n'
    for row in tdm.rows(cutoff=1):
        print row

def splitby_example():
    # The splitby function in the textmining package is very useful. It
    # allows for flexible chunking of a long text document into smaller
    # groups of lines according to a user-defined split function.

    # First let's use the default split function which splits a sequence
    # of lines into groups corresponding to paragraphs. The function
    # defines a paragraph boundary to lie between a non-blank line and
    # blank line.
    text = """

    Hello there
    how are you today?

    I hope you
    are doing well.

    Thanks for using the textmining module!


    """
    lines = text.splitlines()
    print '\nsplitby_example 1\n'
    for paragraph in textmining.splitby(lines):
        # paragraph is a list of lines.
        # Notice that the last paragraph will just contain
        # lines of spaces as there is no text in it.
        print paragraph

    # Now let's use a custom split function to process a more complicated
    # document structure. We want to extract three cleaned-up documents
    # from the following messy text string (this is a common preprocessing
    # task in text mining!)
    text = """

    Document One:
    -------------

    First line of Document One
    Second line of Document One

    Third line of Document One

    Document Two:
    -------------

    First line of Document Two

    Second line of Document Two
    Document Three:
    ---------------
    First line of Document Three


    """

    # Define new split function for this special document structure.
    def document_boundary(line1, line2):
        return line2.strip().startswith('Document')

    # Loop over documents
    lines = text.splitlines()
    print '\nsplitby_example 2\n'
    for document in textmining.splitby(lines, document_boundary):
        # Skip if first line (document[0]) doesn't match document structure
        if not document[0].strip().startswith('Document'):
            continue
        # document is a list of lines. Remove blank lines and strip out
        # whitespace to create a clean document.
        clean_lines = [line.strip() for line in document if line.strip()]
        # Print out clean document
        print '\n'.join(clean_lines)
        print

def dictionary_example():
    # Print ten most common words in the dictionary
    freq_word = [(counts[0][0], word) for (word, counts) in \
      textmining.dictionary.items()]
    freq_word.sort(reverse=True)
    print '\ndictionary_example 1\n'
    for freq, word in freq_word[:10]:
        print word, freq

    # The same word can be used in many different contexts in the English
    # language. The dictionary in the textmining module contains the
    # relative frequencies of each of these parts of speech for a given
    # word. An explanation of the part-of-speech codes is in
    # doc/poscodes.html. Here are the part-of-speech frequencies for the
    # word 'open'.
    print '\ndictionary_example 2\n'
    print textmining.dictionary['open']

def names_example():
    # The textmining module contains three dictionaries of names:
    # names_male, names_female and names_last. Keys are names, values are
    # percent frequency of occurence in US census. 

    # Find relative frequency of some male names
    print '\nnames_example 1\n'
    for name in ('john', 'tom', 'william', 'boris'):
        freq = textmining.names_male[name]
        print name, freq

    # Find 10 most common last names
    f = [(freq, name) for (name, freq) in textmining.names_last.items()]
    f.sort(reverse=True)
    print '\nnames_example 2\n'
    for freq, name in f[:10]:
        print name, freq

def bigram_collocations_example():
    # Find the 10 most statistically significant two word phrases in the
    # full text of 'The Adventures of Sherlock Holmes'
    example_dir = os.path.dirname(__file__)
    sample_text_file = os.path.join(example_dir, 'holmes.txt')
    text = open(sample_text_file).read()
    words = textmining.simple_tokenize(text)
    bigrams = textmining.bigram_collocations(words)
    print '\nbigram_collocations_example 1\n'
    for bigram in bigrams[:10]:
        print ' '.join(bigram)

# Run each of the examples
termdocumentmatrix_example()
splitby_example()
dictionary_example()
names_example()
bigram_collocations_example()
