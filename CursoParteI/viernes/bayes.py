#BAYES teroema
import sklearn
import io
import os
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def dataFrameFromDirectory(path,classification):
    rows = []
    index = []
    for filename, message in readFiles(path):
        rows.append({'message': message, 'class' : classification})
        index.append(filename)
        
    return DataFrame(rows, index = index)
    
    
def readFiles(path):
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            path = os.path.join(root, filename)
            inBody = False
            lines = []
            f = io.open(path, 'r', encoding = 'latin1')
            for line in f:
                if inBody:
                    lines.append(line)
                elif line == '\n':
                    inBody = True
                    
            f.close()
            message = '\n'.join(lines)
            yield path,message
                        

        
data = DataFrame({'message': [], 'class' : []})
data = data.append(dataFrameFromDirectory('emails/spam','spam'))
data = data.append(dataFrameFromDirectory('emails/ham','ham'))

def resultado(train,test):
    vectorizer = CountVectorizer()
    counts = vectorizer.fit_transform(data['message'][:train].values)
    classifier = MultinomialNB()
    targets = data['class'][:train].values
    classifier.fit(counts, targets)


    MultinomialNB(alpha =1.0, class_prior = None, fit_prior = True)
    #examples = ['Free viagra now!!!','Hi Bob, how about a game of golf tomorrow']
    
    examples = data['message'][test:]
    example_counts = vectorizer.transform(examples)
    predictions = classifier.predict(example_counts)
    x = predictions
    sies= 0 
    noes = 0
    for es in x:        
        if es == 'spam':
            sies += 1
        else: noes += 1
    print (sies,noes)
 
        

