import fasttext
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from wordcloud import WordCloud, STOPWORDS
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
STOPWORDS = list(STOPWORDS)
STOPWORDS.append('I')
STOPWORDS.append("I'm")
def visualize(txtfile):
    model = fasttext.skipgram(txtfile, 'model')
    vectors = []
    for word in model.words:
        vectors.append(model[word])
    tsne = TSNE(n_components=2, random_state=0)
    np.set_printoptions(suppress=True)
    Y = tsne.fit_transform(vectors)
    fig = plt.figure()
    plt.scatter(Y[:, 0], Y[:, 1])
    for label, x, y in zip(model.words, Y[:, 0], Y[:, 1]):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
    fig.savefig(txtfile[:-4]+'1'+'.png')



def cloud(txtfile):
    with open(txtfile) as f:
        lines = f.readlines()
        text = "".join(lines)
    wordcloud = WordCloud(
                          stopwords=STOPWORDS,
                          width=1200,
                          height=1000
                          ).generate(text)
    fig = plt.figure()
    plt.imshow(wordcloud)
    plt.axis('off')
    fig.savefig(txtfile[:-4] +'2'+ '.png')

#filename = 'text_data/Orange.txt'

def histogram(txtfile):
    file = open(txtfile)
    wordcount = {}
    for word in file.read().lower().split():
        if (word not in wordcount) and (word not in STOPWORDS):
            wordcount[word] = 1
        elif word not in STOPWORDS:
            wordcount[word] += 1
    final = dict((k, v) for k, v in wordcount.iteritems() if v > 5)
    fig = plt.figure()
    plt.bar(range(len(final)), final.values(), align='center')
    plt.xticks(range(len(final)), final.keys(), rotation=90)
    plt.tight_layout()
    fig.savefig(txtfile[:-4] +'3'+'.png')


first_dirs= ['text_data/'+x for x in os.listdir("text_data") if x.endswith('.txt')]
second_dirs = ['text_data2/'+x for x in os.listdir("text_data2") if x.endswith('.txt')]

for file in first_dirs:
    #visualize(file)
    #cloud(file)
    histogram(file)

for file in second_dirs:
    #visualize(file)
    #cloud(file)
    histogram(file)


#print STOPWORDS

#filen = 'text_data/Sushi.txt'

#visualize(filen)
#cloud(filen)
#histogram(filen)

#print first_dirs
