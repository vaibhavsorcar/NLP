import nltk
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('punkt_tab')
text = """The quick brown fox jumps over the lazy dog. The dog was not amused by the fox's antics."""
tokens = word_tokenize(text.lower())
total_words = len(tokens)
unique_words = len(set(tokens))
word_to_count = 'the'
the_count = tokens.count(word_to_count)
percentage_the = (the_count / total_words * 100) if total_words > 0 else 0
