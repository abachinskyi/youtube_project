import fasttext
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

def visualize(txtfile):
    model = fasttext.skipgram(txtfile, 'model')
    vectors = []
    for word in model.words:
        vectors.append(model[word])

    tsne = TSNE(n_components=2, random_state=0)
    np.set_printoptions(suppress=True)
    Y = tsne.fit_transform(vectors)
    plt.figure(figsize=(20, 20))
    plt.scatter(Y[:, 0], Y[:, 1])
    for label, x, y in zip(model.words, Y[:, 0], Y[:, 1]):
        plt.annotate(label, xy=(x, y), xytext=(0, 0), textcoords='offset points')
    plt.xlim(-16, 16)
    plt.ylim(-15, 17)
    plt.show()
