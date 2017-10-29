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


#def get_tokens():
#    with open('001.txt') as stopl:
#        tokens = nltk.word_tokenize(stopl.read().lower().translate(string.punctuation))
#        #tokens = nltk.word_tokenize(stopl.read().lower().translate(None, string.punctuation))
#    return tokens

if __name__ == "__main__":

#    tokens = get_tokens()
#    #print("tokens[:20]=%s") %(tokens[:20])
#    print("tokens[:20]=%s" %(tokens[:20]))
#    
#    count1 = Counter(tokens)
#    #print("before: len(count1) = %s") %(len(count1))
#    print("before: len(count1) = %s" %(len(count1))) 
#    
#    filtered1 = [w for w in tokens if not w in stopwords.words('english')]
#
#    print("filtered1 tokens[:20]=%s" %(filtered1[:20]))
#    
#    count1 = Counter(filtered1)
#    print("after: len(count1) = %s" %(len(count1)))
#    
#    print("most_common = %s" %(count1.most_common(10)))
#
#    tagged1 = nltk.pos_tag(filtered1)
#    print("tagged1[:20]=%s" %(tagged1[:20]))

    stopwords = nltk.corpus.stopwords.words('english')
    tokenizer = RegexpTokenizer("[\w']+", flags=re.UNICODE)

    #def freq(word, tokens):
    #    return tokens.count(word)
    
    #def word_count(tokens):
    #    return len(tokens)

    #def tf(word, tokens):
    #    return (freq(word, tokens) / float(word_count(tokens)))

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
        return math.log(len(list_of_docs) / float(num_docs_containing(word, list_of_docs)))
    
    
    vocabulary = []
    docs = {}
    all_tips = []

    
    with open('001.txt') as stopl:
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

    docs[doc_a] = {'freq': {}, 'tf': {}, 'idf': {}}
    
    for token in ftokens:
        docs[doc_a]['freq'][token] = freq(token, ftokens)
        docs[doc_a]['tf'][token] = tf(token, ftokens)

    vocabulary.append(ftokens)

    for doc in docs:
        for token in docs[doc]['tf']:
            docs[doc]['idf'][token] = idf(token, vocabulary)
        
    print(docs)
