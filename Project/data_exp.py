import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from gensim.parsing.preprocessing import remove_stopwords
# from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')


if __name__ == "__main__":
    data = pd.read_csv("./database/fake.csv")
    textos = data['text'].values
    stopwords = nltk.corpus.stopwords.words('portuguese')
    print(stopwords)
    # print(x for x in textos[1] if x not in stopwords.words('portuguese'))
    # texts = [remove_stopwords(text) for text in textos]
    