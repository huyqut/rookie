from nltk.book import *
from __future__ import  division
from nltk import bigrams

# nltk.download()  # Invoke UI to download necessary data for nltk

print(text1)
text1.concordance('monstrous')  # Search for a word in text and show its context
text2.concordance('affection')
text3.concordance('lived')

text1.similar('monstrous')  # Other words that contain similar context to 'monstrous'
text2.similar('monstrous')

text2.common_contexts(['monstrous', 'very'])  # Contexts that serve both 'monstrous' and 'very'
text2.common_contexts(['beautiful', 'tender'])

# Location of a word = # of words appear before it
# Dispersion plot: vertical = words to be counted, horizontal = # of words in the document
# Each appearance of a word in the document mark a stripe
text4.dispersion_plot(['citizens', 'democracy', 'freedom', 'duties', 'America'])

# Generate a bunch of random words/text
text3.generate()  # Currently broke (https://github.com/nltk/nltk/issues/736)

# Number of words in a text
print(len(text3))

# Vocabulary of a text (apply set to the text)
print(len(set(text3)))

# Lexical richness = # tokens / # vocabulary
print(len(text3) / len(set(text3)))

# Percentage of a word in a document:
print(100 * text3.count('is') / len(text3))


# Frequency Distribution of a word
fdist = FreqDist(text1)
vocab = fdist.keys()  # All distinct vocabularies in the text
moby_count = fdist['Moby']  # Count of moby
fdist.plot(50, cumulative = True)  # ver = % in text, hor = vocab, cumulative = add % of 1 word after another
fdist.hapaxes()  # Words that count only once
fdist.N()  # Total # of samples (words)
fdist.freq('Mobdy')  # Frequency of a word
fdist.max()  # Word with maximum count (occurs most)
result = [word for word in fdist]  # Iterate the words

# Collocation: bi-gram that occurs unusually more often (and words are usually rare)
list(bigrams(['more', 'is', 'said', 'than', 'done']))
text1.collocations()
text8.collocations()
