from sklearn import svm, datasets
from sklearn.datasets import load_digits
import numpy as np
import random
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
import matplotlib.pyplot as plt
import urllib
import csv



def plot(X_test, predict, accuracy, title):
    x = []
    y = []
    colors = []
    s = 121

    for i in range(0, len(X_test)):
        temp = X_test[i]
        x.append(temp[0])
        y.append(temp[1])


        if(predict[i] == 1):
            colors.append('red')
        else:
            colors.append('blue')

    plt.scatter(x, y, c=colors, s=s)
    plt.ylim(min(y)-0.5,max(y)+0.5)
    plt.xlim(min(x)-0.5,max(x)+0.5)
    plt.title(title, loc="left")
    plt.title(accuracy, loc="right")
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())

    #plt.show()
    plt.savefig(title, bbox_inches='tight')
    plt.close()

def plot_true(X_test, predict):
    x = []
    y = []
    colors = []
    s = 121

    for i in range(0, len(X_test)):
        temp = X_test[i]
        x.append(temp[0])
        y.append(temp[1])


        if(predict[i] == 1):
            colors.append('red')
        else:
            colors.append('blue')

    plt.scatter(x, y, c=colors, s=s)
    plt.ylim(min(y)-1,max(y)+1)
    plt.xlim(min(x)-1,max(x)+1)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig("true", bbox_inches='tight')
    plt.close()


def linear_svm():
    reg_para  = 1.0
    lsvm = svm.LinearSVC(C=reg_para).fit(X_train, y_train)
    predict = lsvm.predict(X_test)
    accuracy = accuracy_score(y_test, predict)

    #plot(X_test, predict, accuracy, "LinearSVM")
    return predict


def kNeighbors():
    knn = KNeighborsClassifier().fit(X_train, y_train)
    predict = knn.predict(X_test)
    accuracy = accuracy_score(y_test, predict)

    #plot(X_test, predict, accuracy, "KNN")
    return predict


def naive_bayes():
    nb = GaussianNB().fit(X_train, y_train)
    predict = nb.predict(X_test)
    accuracy = accuracy_score(y_test, predict)

    #plot(X_test, predict, accuracy, "NaiveBayes")
    return predict


def decision_tree():
    dt = tree.DecisionTreeClassifier().fit(X_train, y_train)
    predict = dt.predict(X_test)
    accuracy = accuracy_score(y_test, predict)

    #plot(X_test, predict, accuracy, "DecisionTrees")
    return predict






#get the data
# iris = datasets.load_iris()
# data = iris.data[:100]
# target = iris.target[:100]
#
# #70% train, 30% test
# np.random.seed(0)
# indices = np.random.permutation(len(data))
# X_train = data[indices[:-30]]
# y_train = target[indices[:-30]]
# X_test = data[indices[:30]]
# y_test = target[indices[:30]]


#Prima Indian datasets

url = "http://goo.gl/j0Rvxq"
raw_data = urllib.urlopen(url)

pima = np.loadtxt(raw_data, delimiter=",")
data = pima[:,0:7]
target = pima[:,8]

#70% train, 30% test
np.random.seed(0)
indices = np.random.permutation(len(data))
X_train = data[indices[:-30]]
y_train = target[indices[:-30]]
X_test = data[indices[:30]]
y_test = target[indices[:30]]

ll = linear_svm()
knn = kNeighbors()
nb = naive_bayes()
dt = decision_tree()

#plot_true(X_test, y_test)


with open('data.csv', 'wb') as output:
    csvwriter = csv.writer(output)
    csvwriter.writerow(['x','y','ll','knn','nb','dt','true'])

    for x in range(0, len(X_test)):
        temp = X_test[x]
        #output.write(str(temp[0])+','+str(temp[1])+','+str(ll[x])+','+str(knn[x])+','+str(nb[x])+','+str(dt[x])+','+y_test[x])
        csvwriter.writerow([ str(temp[0]) , str(temp[1]), str(ll[x]), str(knn[x]), str(nb[x]), str(dt[x]), str(y_test[x]) ])
