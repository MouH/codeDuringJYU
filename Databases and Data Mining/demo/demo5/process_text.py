import cPickle as p
import matplotlib.pyplot as plt
from math import *
import re

f = file("./text")
texts = p.load(f)
print "initiate " + str(len(texts)) + " message"

total_number_of_message = len(texts)
# for i in text[:5]:
# 	print i
corpus = {}
# compute the how many times different word  showed in different tweets
for text in texts:
    a = []
    for i in re.split('[^A-Za-z0-9]', text):
    	if i in a:
            continue
        else:
            a.append(i)
            if i in corpus:
                corpus[i] += 1
            else:
                corpus[i] = 1
print "\n"
print "get whole corpus of total " + str(len(corpus.keys())) + " words"

key_words = {}
#help function
def count_word_frequence(from_text):
    probability = {}
    words = re.split('[^A-Za-z0-9]', from_text)
    for word in words:
        if word != '':
            if word in probability:
                probability[word] += 1
            else:
                probability[word] = 1
    return probability


for text in texts:
    frequence = count_word_frequence(text)
    key1 = (0,'') 
    key2 = (0,'')
    for word in frequence:
        idf = log(total_number_of_message / corpus[word], 2)
        tf_idf = frequence[word] * idf
        if tf_idf > key1[0]:
            key2 = key1
            key1 = (tf_idf, word)
        elif tf_idf > key2[0]:
            key2 = (tf_idf, word)
    key_words[text] = (key1, key2)

for keyword in key_words:
    try:
        print keyword
        print key_words[keyword]
        print "\n"
    except Exception, e:
        pass
    

