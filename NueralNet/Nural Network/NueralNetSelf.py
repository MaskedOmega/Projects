import numpy as np
import pandas as pd
from PIL import Image
from matplotlib import pyplot as plt



data = Image.open('Images/1.png')
data = np.array(data)
data = ((np.sum(data, axis=2))/4)/300
data=np.concatenate(data, axis=0 )

Sizearr=(data.size)
nodes=10

####
#w = np.arange(Sizearr)
#w2 = np.arange(nodes)
#b = np.zeros(Sizearr)
#b2 = np.zeros(nodes)
#print(w2)

#def savedata(data,FileName,Type):
    #np.save(Type+ "/" + str(FileName)+ ".npy",data)

#arr1w=savedata(w,"Weights1","Weights")
#arr2w=savedata(W2,"Weights2","Weights")
#arr1b=savedata(b,"Bias1","Bias")
#arr2b=savedata(b2,"Bias2","Bias")

###

w=np.load("Weights/Weights1.npy") 
b=np.load("Bias/Bias1.npy") 

w2=np.load("Weights/Weights2.npy") 
b2=np.load("Bias/Bias2.npy") 


def ReLU(data):
    return np.maximum(data, 0)

def softmax(data):
    data = np.exp(data) / sum(np.exp(data))
    return data


def FowardPropergation(data,w,b,w2,b2):
    z1=w.dot(data) + b
    a1=ReLU(z1)
    print(a1)
    z2=w2.dot(a1) + b2
    a2=softmax(z2)
    return(a2)

def get_predictions(A2):
    return np.argmax(A2, 0)

def make_predictions(X, w1, b1, w2, b2):
    _, _, _, A2 = FowardPropergation(w1, b1, w2, b2, X)
    predictions = get_predictions(A2)
    return predictions

def test_prediction(data):
    current_image = data.reshape((28, 28)) * 255
    print(data)
    plt.gray()
    plt.imshow(current_image, interpolation='nearest')
    plt.show()


#test_prediction(data)
make_predictions(data, w, b, w2, nodes)