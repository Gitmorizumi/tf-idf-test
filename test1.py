import nltk
from nltk.corpus import stopwords

def not_stopwords(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)

print(not_stopwords(nltk.corpus.reuters.words()))

#print(stopwords.words('english'))
