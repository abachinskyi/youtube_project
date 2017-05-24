import os
from gensim.models import doc2vec
from collections import namedtuple
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np
doc1 = ["This is a sentence", "This is another sentence"]

docs = []
analyzedDocument = namedtuple('AnalyzedDocument', 'words tags')
for i, text in enumerate(doc1):
    words = text.lower().split()
    tags = [i]
    docs.append(analyzedDocument(words, tags))

print docs

#model = doc2vec.Doc2Vec(docs, size = 1000, window = 300, min_count = 1, workers = 4)
#print model.docvecs[0]
#print model.docvecs[1]
docs = []
first_dirs= ['text_data_extended2/'+x for x in os.listdir("text_data_extended2") if x.endswith('.txt')]
analyzedDocuments = namedtuple('AnalyzedDocument', 'words tags')
tags=[]
for file in first_dirs:
    with open(file) as f:
        lines = f.readlines()
        text ="".join(lines)
    words = text.lower().split()
    tag = [file[(file.find('/') + 1):file.find('.')]]
    tags.append(tag[0])
    docs.append(analyzedDocument(words, tag))

model = doc2vec.Doc2Vec(docs, size = 500, window = 400, min_count = 5, workers = 4)

model.docvecs
''' '''
vectors = []
for word in model.docvecs:
    vectors.append(word)
tsne = TSNE(n_components=2, random_state=0)
np.set_printoptions(suppress=True)
Y = tsne.fit_transform(vectors)
fig = plt.figure()
plt.scatter(Y[:, 0]*10000, Y[:, 1]*10000)
for label, x, y in zip(tags, Y[:, 0]*10000, Y[:, 1]*10000):
    plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
plt.show()
