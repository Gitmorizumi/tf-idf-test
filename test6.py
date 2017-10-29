import nltk
from collections import Counter
import string
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
import re
from nltk import bigrams
from nltk import trigrams
import math

#nltk.download()

if __name__ == "__main__":

    stopwords = nltk.corpus.stopwords.words('english')
    tokenizer = RegexpTokenizer("[\w']+", flags=re.UNICODE)

    def freq(word, doc):
        return doc.count(word)

    def word_count(doc):
        return len(doc)

    def tf(word, doc):
        return (freq(word, doc) / float(word_count(doc)))


    def num_docs_containing(word, list_of_docs):
        count = 0
        for document in list_of_docs:
            if freq(word, document) > 0:
                count += 1
                return 1 + count

    def idf(word, list_of_docs):
        return (math.log(len(list_of_docs) / float(num_docs_containing(word, list_of_docs))) + 1)
    
    def tf_idf(word, doc, list_of_docs):
        return (tf(word, doc) * idf(word, list_of_docs))
    
    
    vocabulary = []
    docs = {}
    all_tips = []

    
    with open('013.txt') as stopl:
        doc_a = stopl.read()

    #print(doc_a.lower())

    tokens = tokenizer.tokenize(doc_a)

    bitokens = bigrams(tokens)
    tritokens = trigrams(tokens)
    tokens = [token.lower() for token in tokens if len(token) > 2]
    tokens = [token for token in tokens if token not in stopwords]

    bitokens = [' '.join(token).lower() for token in bitokens]
    bitokens = [token for token in bitokens if token not in stopwords]

    tritokens = [' '.join(token).lower() for token in tritokens]
    tritokens = [token for token in tritokens if token not in stopwords]

    ftokens = []
    ftokens.extend(tokens)
    ftokens.extend(bitokens)
    ftokens.extend(tritokens)

    #docs[doc_a] = {'freq': {}}
    #docs[doc_a] = {'freq': {}, 'tf':{}}

    docs[doc_a] = {'freq': {}, 'tf': {}, 'idf': {}, 'tf-idf': {}, 'tokens': {}}
    
    for token in ftokens:
        docs[doc_a]['freq'][token] = freq(token, ftokens)
        docs[doc_a]['tf'][token] = tf(token, ftokens)
        docs[doc_a]['tokens'] = ftokens

    vocabulary.append(ftokens)

    for doc in docs:
        for token in docs[doc]['tf']:
            docs[doc]['idf'][token] = idf(token, vocabulary)
            docs[doc]['tf-idf'][token] = tf_idf(token, docs[doc]['tokens'], vocabulary)

    words = {}
    for doc in docs:
        for token in docs[doc]['tf-idf']:
            if token not in words:
                words[token] = docs[doc]['tf-idf'][token]
            else:
                if docs[doc]['tf-idf'][token] > words[token]:
                    words[token] = docs[doc]['tf-idf'][token]
                    

    for item in sorted(words.items(), key=lambda x: x[1], reverse=True):
        print ("%f <= %s" % (item[1], item[0]))
