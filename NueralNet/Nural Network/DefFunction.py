from re import A
from turtle import xcor
import xdrlib
from zipfile import ZIP_BZIP2
import numpy as np
from PIL import Image
import pandas as pd
from matplotlib import pyplot as plt
from time import sleep
import time


#geting the image data
img_data = Image.open('2.png')
CorrectChoice=1
img_arr = np.array(img_data)
TotalSize_arr=(img_arr.size)
new_a = ((np.sum(img_arr, axis=2))/4)/300
new_a=np.concatenate(new_a, axis=0 )
TotalSize_arr=(new_a.size)
#print(img_arr)
#print(new_a)
#print(TotalSize_arr)


X_train=[new_a]
Y_train = new_a


def init_params():
    W1 = np.random.rand(10, TotalSize_arr) - 0.5
    b1 = np.random.rand(10, 1) - 0.5
    W2 = np.random.rand(10, 10) - 0.5
    b2 = np.random.rand(10, 1) - 0.5
    return W1, b1, W2, b2

def ReLU(Z):
    return np.maximum(Z, 0)

def softmax(Z):
    A = np.exp(Z) / sum(np.exp(Z))
    return A
    
def forward_prop(W1, b1, W2, b2, X):
    Z1 = W1.dot(X) + b1
    print(Z1)
    A1 = ReLU(Z1)
    Z2 = W2.dot(A1) + b2
    A2 = softmax(Z2)
    return Z1, A1, Z2, A2

def get_predictions(A2):
    return np.argmax(A2, 0)

def make_predictions(X, W1, b1, W2, b2):
    _, _, _, A2 = forward_prop(W1, b1, W2, b2, X)
    predictions = get_predictions(A2)
    return predictions

def test_prediction(index, W1, b1, W2, b2):
    current_image = (X_train[index])[:, None]
    prediction = make_predictions((X_train[index])[:, None], W1, b1, W2, b2)
    label = Y_train[index]
    print("Prediction: ", prediction)
    print("Label: ", label)
    
    current_image = current_image.reshape((28, 28)) * 255
    plt.gray()
    plt.imshow(current_image, interpolation='nearest')
    plt.show()



W1=np.load("Weights/Weights1.npy") 
W2=np.load("Weights/Weights2.npy") 
b1=np.load("Bias/Bias1.npy") 
b2=np.load("Bias/Bias2.npy") 


FPRun = test_prediction(0, W1, b1, W2, b2)
print(FPRun)
current_image = FPRun.reshape((28, 28)) * 255
plt.gray()
a=plt.imshow(current_image, interpolation='nearest')












