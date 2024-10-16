import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

text = """Natural Language Processing is a fascinating area of Artificial Intelligence and Machine Learning. It allows machines to understand and generate human language."""
tokens = word_tokenize(text.lower())
filtered_tokens = [word for word in tokens if word.isalnum() and word not in stopwords.words('english')]

print(filtered_tokens)
