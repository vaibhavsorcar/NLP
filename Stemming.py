import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
nltk.download('punkt')
text = """Natural Language Processing allows computers to understand human languages. Tokenization splits the text into words, and stemming reduces words to their base forms."""
tokens = word_tokenize(text.lower())
stemmed_tokens = [PorterStemmer().stem(token) for token in tokens]
print("Original Tokens:", tokens)
print("Stemmed Tokens:", stemmed_tokens)
