import nltk
from collections import Counter
import string
from nltk.corpus import stopwords
#nltk.download()

def get_tokens():
    with open('001.txt') as stopl:
        tokens = nltk.word_tokenize(stopl.read().lower().translate(string.punctuation))
        #tokens = nltk.word_tokenize(stopl.read().lower().translate(None, string.punctuation))
    return tokens

if __name__ == "__main__":

    tokens = get_tokens()
    #print("tokens[:20]=%s") %(tokens[:20])
    print("tokens[:20]=%s" %(tokens[:20]))
    
    count1 = Counter(tokens)
    #print("before: len(count1) = %s") %(len(count1))
    print("before: len(count1) = %s" %(len(count1))) 
    
    filtered1 = [w for w in tokens if not w in stopwords.words('english')]

    print("filtered1 tokens[:20]=%s" %(filtered1[:20]))
    
    count1 = Counter(filtered1)
    print("after: len(count1) = %s" %(len(count1)))
    
    print("most_common = %s" %(count1.most_common(10)))

    tagged1 = nltk.pos_tag(filtered1)
    print("tagged1[:20]=%s" %(tagged1[:20]))
