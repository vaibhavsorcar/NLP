import nltk
from nltk.corpus import brown
nltk.download('brown')
brown_text = nltk.Text(brown.words())
def find_concordances(word, width=80, lines=25):
    print(f"Concordances for '{word}':\n")
    brown_text.concordance(word, width=width, lines=lines)
find_concordances(input("Enter a word to find concordances: "))
