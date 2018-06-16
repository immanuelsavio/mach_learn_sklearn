import matplotlib.pyplot as  plt
from sklearn import datasets 
from sklearn import svm
import numpy as np 

digits = datasets.load_digits()

clf = svm.SVC(gamma=0.001, C=100) #increase gamma for more accuracy

x,y = digits.data[:-10], digits.target[:-10] #dont Edit this number 
clf.fit(x,y)

print('Prediction:',clf.predict(digits.data[[-2]]))#Edit this number for more examples

plt.imshow(digits.images[-2], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()
