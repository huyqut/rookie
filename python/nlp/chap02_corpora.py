import nltk

nltk.corpus.gutenberg.fileids()  # ID of Gutenberg corpora
emma = nltk.corpus.gutenberg.words('austen-emma.txt')
print(len(emma))

