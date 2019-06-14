

import nltk
import re
from nltk.corpus import stopwords

#import essay data documents

import csv
essay_data=[]
with open('Raw_Data\essays.csv','r') as myfile:
    myreader=csv.reader(myfile, delimiter=',',escapechar='\\', quotechar='"')
    for i,row in enumerate(myreader):
        if i==0:
            header=row
            continue
        if row==[]:
            continue
        essay_data.append(row)

test_essay=essay_data[0][1]


#BASIC TEXT CLEANING FUNCTIONS
#standardize text, tokenize, remove stopwords

#lowercase, remove unneeded features
text=test_essay.lower()   #upper(), capitalize()
text=text.replace('\n',' ')

#tokenize
tokens = nltk.word_tokenize(text)
#or
tokens = re.findall(r'[\d\w]+',text)

#stopwords
tokens_clean=[]
for word in tokens:
    if word not in stopwords.words('english'):
        tokens_clean.append(word)

#or - List comprehensions!
tokens_clean = [word for word in tokens if word not in stopwords.words('english')]

#part of speech
#use the nltk pos function to tag the tokens
tagged_tokens = nltk.pos_tag(tokens_clean)
#pull out adjectives
adjectives = [word for word,pos in tagged_tokens if pos == 'JJ' or pos=='JJR' or pos=='JJS']
nouns = [word for word,pos in tagged_tokens if pos=='NN' or pos=='NNS']
freq_nouns=nltk.FreqDist(nouns)
print(adjectives)
#view new variable
print(tagged_sentence_tokens)


#BASIC TEXT STATISTICS 
wordFrequency=nltk.FreqDist(sentence_tokens)
print(wordFrequency.most_common(10))
print(len(wordFrequency))


#ADVANCED TEXT FUNCTIONS
#collocations
text1_nltk = nltk.Text(text1_tokens)
text1_nltk.concordance("monstrous")

#VISUALIZE THE RESULTS



#VECTORIZING

def tokenize(text, stopwords=[]): #default of stopwords is empty list
    '''This is the documentation for tokenize at least in ipython'''
    text = text.lower()       #this makes all text lowercase
    pat = "[\d\w']+"        #match anything that is digit or word character. + one or more
    text = re.findall(pat,text) #splits on re pattern 'pat' in text
    
    tokens=[]
    for w in text:
        if w not in stopwords:  #case sensitive, must input whole word. will not eject 'time' if 'i' in list
            tokens.append(w)       #could say res += [w]
    
    return tokens                


def make_tfidf(corpus, stopwords=[], dfExp=0.5):        
    print ('tokenizing')
    termsList = []
    for t in corpus:
        theseTerms=tokenize(t, stopwords)
        termList.append(theseTerms)
    
    allTerms=set()
    for i in termList:
        allTerms.update(i)
    allTerms = list(allTerms)       #make uniqe set indexable
    
    allTermsDict = dict(zip(allTerms, range(len(allTerms))))

    vspace = scipy.zeros((len(corpus), len(allTerms)), dtype='float64')
    #uses () for tuple, create matrix of zeros, (row, column). define them as
    #floating     #points of 64 bits (default is also float64). 
    #Float allows for high precision calculation
                
    
    
    for i,v in enumerate(termsList):
        terms=termsList[i]
        for v in terms:
            vspace[i,allTermsDict[v]] +=1 #if term is already found, add one to cell
    
    docFreq = scipy.sum(vspace>0,0)       #sum all columns (here columns are individual documents. Result is num of times word in doc)
    docFreq= docFreq**dfExp     #square root docFreq is weighting heuristic
    vspace = vspace/docFreq        #result is tf/idf
    
    #normalize (for theta measure):
    sumSqrs=scipy.sum(vspace**2,1)
    magn=scipy.sqrt(sumSqrs)                #normalize tf/idf -> magnitude of location in vector space
    magn=magn.reshape(len(corpus),1)        #makes magn a column, instead of row)
    vspace= vspace/magn                     #
    return (allTerms, vspace)               #Term, normalized vector-space weight
    
